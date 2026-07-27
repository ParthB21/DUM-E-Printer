#!/usr/bin/env python3
"""
DUM-E keyboard jog — demo control for the working motors.

  Shoulder pitch  Z
  Wrist pitch     Y
  Wrist roll      A
  Extruder        E

Close any other serial monitor (PlatformIO, Pronterface) first.

Usage:
  pip install pyserial
  python tools/keyboard_jog.py              # auto-pick a COM port
  python tools/keyboard_jog.py COM5
  python tools/keyboard_jog.py COM5 --cold-extrude
"""

from __future__ import annotations

import argparse
import sys
import time

try:
    import serial
    from serial.tools import list_ports
except ImportError:
    print("Install pyserial first:  pip install pyserial")
    sys.exit(1)

if sys.platform == "win32":
    import msvcrt
else:
    import select
    import termios
    import tty


BAUD = 115200
JOINT_STEP = 5.0      # degrees-ish per keypress (Y / Z / A)
EXTRUDE_STEP = 2.0    # mm filament per keypress
FEED_JOINT = 1800       # F for shoulder pitch and wrist roll
FEED_WRIST_PITCH = 1800 # F for wrist pitch
FEED_E = 1800           # F for extruder

HELP = """
Keys (hold or tap):
  Up / Down       shoulder pitch  (Z)
  Left / Right    wrist pitch     (Y)
  A / D           wrist roll      (A)
  E / Q           extruder        (E)  feed / retract

  + / -     bigger / smaller joint step
  [ / ]     bigger / smaller extrude step
  Space     disable motors (M18)
  Enter     enable motors  (M17)
  H         reprint this help
  Esc / X   quit
"""


def pick_port(preferred: str | None) -> str:
    if preferred:
        return preferred
    ports = list(list_ports.comports())
    if not ports:
        print("No serial ports found. Plug in the board USB and try again.")
        sys.exit(1)
    print("Available ports:")
    for i, p in enumerate(ports):
        print(f"  [{i}] {p.device:8}  {p.description}")
    if len(ports) == 1:
        print(f"Using {ports[0].device}")
        return ports[0].device
    choice = input("Port number: ").strip()
    try:
        return ports[int(choice)].device
    except (ValueError, IndexError):
        print("Invalid choice.")
        sys.exit(1)


def send(ser: serial.Serial, line: str, wait_ok: bool = True) -> None:
    cmd = (line.strip() + "\n").encode("ascii")
    ser.write(cmd)
    ser.flush()
    print(f">>> {line.strip()}")
    if not wait_ok:
        return
    deadline = time.time() + 3.0
    while time.time() < deadline:
        raw = ser.readline().decode("utf-8", errors="replace").strip()
        if not raw:
            continue
        print(f"    {raw}")
        low = raw.lower()
        if low.startswith("ok") or "error" in low or "echo:busy" in low:
            return
    print("    (no ok — continuing)")


def read_key() -> str | None:
    """Return a single logical key name, or None if nothing pressed."""
    if sys.platform == "win32":
        if not msvcrt.kbhit():
            return None
        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            code = msvcrt.getch()
            arrows = {b"H": "up", b"P": "down", b"K": "left", b"M": "right"}
            return arrows.get(code)
        if ch == b"\r":
            return "enter"
        if ch == b" ":
            return "space"
        if ch == b"\x1b":
            return "esc"
        try:
            return ch.decode("ascii").lower()
        except UnicodeDecodeError:
            return None

    # POSIX: non-blocking single char / arrow escape
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if not dr:
        return None
    ch = sys.stdin.read(1)
    if ch == "\x1b":
        if select.select([sys.stdin], [], [], 0.01)[0]:
            rest = sys.stdin.read(2)
            arrows = {"[A": "up", "[B": "down", "[D": "left", "[C": "right"}
            return arrows.get(rest, "esc")
        return "esc"
    if ch == "\n":
        return "enter"
    if ch == " ":
        return "space"
    return ch.lower()


def main() -> None:
    ap = argparse.ArgumentParser(description="DUM-E keyboard jog (Y/Z/A/E)")
    ap.add_argument("port", nargs="?", help="Serial port, e.g. COM5")
    ap.add_argument("--cold-extrude", action="store_true",
                    help="Allow extruder moves without heating (M302 P1)")
    ap.add_argument("--step", type=float, default=JOINT_STEP,
                    help=f"Joint step degrees (default {JOINT_STEP})")
    ap.add_argument("--estep", type=float, default=EXTRUDE_STEP,
                    help=f"Extrude step mm (default {EXTRUDE_STEP})")
    args = ap.parse_args()

    port = pick_port(args.port)
    joint_step = args.step
    estep = args.estep

    print(f"Opening {port} @ {BAUD} …")
    ser = serial.Serial(port, BAUD, timeout=0.2)
    time.sleep(2.0)  # board may reset on open
    ser.reset_input_buffer()

    send(ser, "M115")
    send(ser, "M17")
    send(ser, "G91")   # relative joints
    send(ser, "M83")   # relative extruder (G91 alone does not do this)
    if args.cold_extrude:
        send(ser, "M302 P1")
        print("Cold extrusion enabled for demo.")

    print(HELP)
    print(f"Joint step = {joint_step}°   Extrude step = {estep} mm")
    print("Ready. Keep a hand on the power switch.\n")

    old_term = None
    if sys.platform != "win32":
        old_term = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    moves = {
        "up": ("Z", +1, "shoulder pitch +"),
        "down": ("Z", -1, "shoulder pitch -"),
        "left": ("Y", -1, "wrist pitch -"),
        "right": ("Y", +1, "wrist pitch +"),
        "a": ("A", -1, "wrist roll -"),
        "d": ("A", +1, "wrist roll +"),
        "e": ("E", +1, "extrude +"),
        "q": ("E", -1, "extrude -"),
    }

    try:
        while True:
            key = read_key()
            if key is None:
                # drain any unsolicited serial lines
                while ser.in_waiting:
                    line = ser.readline().decode("utf-8", errors="replace").strip()
                    if line:
                        print(f"    {line}")
                time.sleep(0.02)
                continue

            if key in ("esc", "x"):
                print("Quit.")
                break
            if key == "h":
                print(HELP)
                continue
            if key == "space":
                send(ser, "M18")
                continue
            if key == "enter":
                send(ser, "M17")
                continue
            if key == "+":
                joint_step = min(45.0, joint_step + 1.0)
                print(f"Joint step = {joint_step}°")
                continue
            if key == "-":
                joint_step = max(0.5, joint_step - 1.0)
                print(f"Joint step = {joint_step}°")
                continue
            if key == "]":
                estep = min(20.0, estep + 1.0)
                print(f"Extrude step = {estep} mm")
                continue
            if key == "[":
                estep = max(0.5, estep - 0.5)
                print(f"Extrude step = {estep} mm")
                continue

            if key in moves:
                axis, sign, label = moves[key]
                if axis == "E":
                    dist = sign * estep
                    feed = FEED_E
                else:
                    dist = sign * joint_step
                    feed = FEED_WRIST_PITCH if axis == "Y" else FEED_JOINT
                # Format without trailing junk; A must stay A (not I)
                g = f"G1 {axis}{dist:.2f} F{feed}"
                print(f"[{label}]")
                send(ser, g)
                # small debounce so one tap ≠ ten moves
                time.sleep(0.08)
                while read_key() is not None:
                    pass
    finally:
        if old_term is not None:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_term)
        try:
            send(ser, "M18", wait_ok=False)
        except Exception:
            pass
        ser.close()


if __name__ == "__main__":
    main()
