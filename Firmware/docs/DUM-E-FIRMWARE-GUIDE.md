# DUM-E — Step-by-step bring-up

Follow the steps **in order**. Do not skip ahead to heating or homing until the earlier steps pass.

**What this robot can do right now:** move four joints (yaw, shoulder pitch, wrist pitch, wrist roll) and run the extruder. It is **not** a normal Cartesian printer yet. When you send `G1 X10`, that means “move shoulder yaw by about 10 degrees,” **not** “move 10 mm in X.”

---

## Quick map (keep this nearby)


| Motor plug on board            | What it moves     | Command letter |
| ------------------------------ | ----------------- | -------------- |
| **X**                          | Shoulder yaw      | `X`            |
| **Y**                          | Wrist pitch       | `Y`            |
| **Z** (Z0 and Z1 = same motor) | Shoulder pitch    | `Z`            |
| **E0**                         | Wrist roll        | `A`            |
| **E1**                         | Filament extruder | `E`            |


---

# STEP 1 — Safety before anything moves

1. Put the arm somewhere it cannot hit the table or itself.
2. Keep your hand on the **24 V power switch** so you can cut power instantly.
3. Prefer the arm **supported** or joints free for the first tiny moves.
4. Do **not** heat the hotend in this step.

**You’re done with Step 1 when:** you can kill power in one second.

---

# STEP 2 — Build the firmware (if you haven’t)

1. Open the folder `Marlin-2.1.2.6` in Cursor / VS Code.
2. Open **Marlin Auto Build** (or PlatformIO).
3. Click **Build** on environment `**mks_robin_nano_v3_1`**.
4. Wait until it says **SUCCESS** (warnings are OK).

**You should see:** green success, file created under  
`.pio/build/mks_robin_nano_v3_1/Robin_nano_v3.bin`

**If it fails:** copy the red errors and ask for help (don’t continue).

**You’re done with Step 2 when:** the `.bin` file exists.

---

# STEP 3 — Put firmware on SD or USB stick

1. Format the SD card or USB stick as **FAT32**.
2. Open the folder:
  `Marlin-2.1.2.6/.pio/build/mks_robin_nano_v3_1/`
3. Copy **both** of these to the **root** of the stick (not in a subfolder):
  - `Robin_nano_v3.bin` (exact name)
  - the whole folder named `assets`
4. Eject the stick safely from the PC.

**You’re done with Step 3 when:** stick root contains `Robin_nano_v3.bin` and `assets/`.

---

# STEP 4 — Flash the board

1. Insert the SD card **or** plug the USB stick into the board’s **USB-A host** port (big flat USB, not the tiny USB-to-PC).
2. Connect the **24 V power supply** and turn it on.
3. Watch the TS35 screen.

**You should see:**

1. An update / progress screen, then
2. The board restarts into the Marlin UI.

**Also check the stick afterward:** `Robin_nano_v3.bin` may be renamed to something like `Robin_nano_v3.CUR` — that means flash worked.

**If the screen stays blank:**

- Confirm `assets` was copied
- Confirm 24 V is on
- Reseat the TS35 cable
- Try a different FAT32 SD card

**You’re done with Step 4 when:** the touchscreen shows a normal Marlin / MKS main screen and the machine name is **DUM-E** (or similar).

---

# STEP 5 — Open serial on the PC (PlatformIO)

This is how you type test commands.

1. Leave **24 V on**.
2. Plug the board’s **small USB** (to PC) into your computer.
3. In Cursor / VS Code with the Marlin project open:
  - PlatformIO sidebar → **PROJECT TASKS** → `mks_robin_nano_v3_1` → **General** → **Monitor**  
  - or click the PlatformIO **serial plug** icon
4. Baud rate is already **115200**.

**You should see:** a terminal window that connects to a COM port (may show `echo:` or be quiet until you type).

**If it says port busy / can’t open:**

- Close Pronterface or any other serial program
- Unplug/replug USB
- Try again

**You’re done with Step 5 when:** the serial monitor stays open without errors.

---

# STEP 6 — Smoke test (no motor moves yet)

In the serial monitor, type each line and press Enter.

### 6.1 — Is firmware alive?

Type:

```text
M115
```

**You should see:** text mentioning Marlin and the board.

### 6.2 — Are temperatures sane?

Type:

```text
M105
```

**You should see:** a hotend temperature near room temperature (e.g. 20–30 °C).  
**Do not** send heat commands yet.

### 6.3 — Can the drivers talk over UART?

Type:

```text
M122
```

**You should see:** driver reports for the axes.  
**Bad sign:** lines like `Unable to communicate` for X/Y/Z/E — stop and fix wiring/config before moving motors.

**You’re done with Step 6 when:** `M115`, `M105`, and `M122` all look healthy.

---

# STEP 7 — Tiny joint moves (direction test)

Still in serial monitor. Move **one joint at a time**. Watch the robot. Be ready to kill power.

First put Marlin in relative mode:

```text
G91
```

### 7.1 — Shoulder yaw (plug X)

```text
G1 X5 F20
```

**You should see:** shoulder yaw move a little.

- Wrong way? Note it as “X inverted” (we’ll fix after).
- No move / skipping? Kill power; note which motor.

### 7.2 — Wrist pitch (plug Y)

```text
G1 Y5 F20
```

### 7.3 — Shoulder pitch (plug Z)

```text
G1 Z5 F20
```

### 7.4 — Wrist roll (plug E0, commanded as A)

```text
G1 A5 F20
```

### 7.5 — Fix wrong directions (if needed)

If a joint moved the wrong way:

1. Open `Marlin/Configuration.h`
2. Find `INVERT_X_DIR`, `INVERT_Y_DIR`, `INVERT_Z_DIR`, `INVERT_I_DIR` (I = wrist roll / A)
3. Change `false` ↔ `true` for that axis only
4. Rebuild (Step 2), reflash (Steps 3–4), retest that one joint

**You’re done with Step 7 when:** each joint moves in a direction you agree is “positive.”

### If motors do NOT move (do this checklist)

Send these **one line at a time** and watch both the reply **and** the motors:

```text
M115
M122
M211 S0
M17
G92 X0 Y0 Z0 A0
G91
G1 X30 F30
```

What each does:


| Command      | Purpose                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| `M122`       | Confirms TMC drivers answer (if “Unable to communicate”, motors won’t work until UART/drivers are fixed) |
| `M211 S0`    | Turn **off** soft endstops (they can silently block moves)                                               |
| `M17`        | **Enable** steppers (motors should feel locked / harder to turn by hand)                                 |
| `G92 ...`    | Set current joint angles to 0 so limits don’t block you                                                  |
| `G1 X30 F30` | Bigger, easier-to-see yaw move                                                                           |


**Check with your hand (power on, after `M17`):**

1. Try to twist the **X** motor shaft / coupling gently.
2. If it feels **free / floppy** → steppers are not enabled or not powered.
3. If it feels **locked** but still doesn’t move on `G1` → note the serial reply and tell me what it said.

**Also confirm physically:**

- 24 V PSU is on (USB alone is not enough for motors)
- Motor plugs are fully seated in **X / Y / Z / E0 / E1**
- You’re testing the motor that matches the command (`X` = shoulder yaw plug)

**Common serial replies:**


| You see                                      | Meaning                                                 |
| -------------------------------------------- | ------------------------------------------------------- |
| `ok` and motor locked but no motion          | Tell me; may be current / wiring / wrong plug           |
| `echo:Unknown command: "G1 A..."`            | Use `G1 I5 F20` instead, or rebuild with I-axis enabled |
| Endstop / homing / “must home” style message | Paste the exact text                                    |
| `Unable to communicate` in `M122`            | Fix TMC UART first — motion won’t work                  |


**Reset settings if an old EEPROM is fighting you:**

```text
M502
M500
M17
G92 X0 Y0 Z0 A0
G91
G1 X30 F30
```

---

# STEP 8 — Calibrate steps (angle accuracy)

You don’t need exact belt ratios. Measure instead.

Example for **X** (do the same idea for Y, Z, A):

1. Mark the joint with tape/pen so you can see rotation.
2. Send:

```text
G91
G1 X90 F30
```

1. Measure how many degrees it **actually** moved (protractor / careful estimate is fine for now).
2. Compute:

`new_steps = old_steps × (90 / measured_degrees)`

Starting values already in firmware:

- X ≈ 124.44  
- Y ≈ 8.89  
- Z ≈ 453.33  
- A ≈ 8.89

1. Apply temporarily over serial (example if new X steps were 200):

```text
M92 X200
M500
```

Or edit `DEFAULT_AXIS_STEPS_PER_UNIT` in `Configuration.h` and rebuild later.

**You’re done with Step 8 when:** commanding ~90° on each joint gets roughly 90° of real motion.

---

# STEP 9 — Wire the 4 endstops (later; skip until motors feel good)

Do this **after** Steps 6–8 feel safe.

### 9.1 — Remove DIAG jumpers

On the Robin Nano, **remove the DIAG jumpers** (needed because you use real endstops, not sensorless).

### 9.2 — Plug endstops


| Board plug | Joint          |
| ---------- | -------------- |
| **X-**     | Shoulder yaw   |
| **Z-**     | Shoulder pitch |
| **Y-**     | Wrist pitch    |
| **Z+**     | Wrist roll     |


Do **not** put an endstop on the extruder.

### 9.3 — Test with M119

```text
M119
```

1. Read the report.
2. Block / unblock one sensor at a time.
3. That line should switch between `open` and `TRIGGERED`.

If a sensor is always wrong / inverted: flip that axis’s `*_ENDSTOP_INVERTING` in `Configuration.h`, rebuild, reflash, retest.

### 9.4 — Homing (only after M119 looks right)

```text
G28
```

Watch carefully; kill power if a joint drives into a hard stop without triggering.

**You’re done with Step 9 when:** all four endstops toggle correctly and a careful `G28` works.

---

# STEP 10 — Hotend (only after motion is trusted)

1. Confirm heater + thermistor wired correctly.
2. Heat:

```text
M104 S200
M105
```

Temp should rise toward 200 °C. If it doesn’t, or errors appear — kill power / stop heating.

1. When stable, optional PID tune:

```text
M303 E0 S200 C8
M500
```

1. Extrusion test (hot enough first): mark filament, then:

```text
G1 E10 F100
```

**You’re done with Step 10 when:** hotend heats controllably and extruder feeds filament.

---

# STEP 11 — What “done for now” means

You are in good shape for early DUM-E testing when:

- [ ] Screen boots to DUM-E UI  
- [ ] `M115` / `M105` / `M122` work  
- [ ] All four joints jog safely with correct directions  
- [ ] Steps are roughly calibrated  
- [ ] (Optional) Endstops + homing work  
- [ ] (Optional) Hotend heats and extrudes  

You are **not** ready to slice a normal STL and print it yet. That needs elbow hardware + real arm kinematics later.

---

## Common serial commands cheat sheet


| Command     | Meaning                         |
| ----------- | ------------------------------- |
| `M115`      | Firmware identity               |
| `M105`      | Temperatures                    |
| `M122`      | TMC driver status               |
| `M119`      | Endstop status                  |
| `G91`       | Relative moves                  |
| `G90`       | Absolute moves                  |
| `G1 X5 F20` | Move yaw ~5° slowly             |
| `G1 A5 F20` | Move wrist roll ~5° slowly      |
| `G28`       | Home (only after endstops work) |
| `M18`       | Disable steppers (motors free)  |
| `M17`       | Enable steppers                 |


---

## Where things live in the repo


| File                         | What you’d edit                                          |
| ---------------------------- | -------------------------------------------------------- |
| `Marlin/Configuration.h`     | Directions (`INVERT_*`), steps, endstop invert, board/UI |
| `Marlin/Configuration_adv.h` | Motor currents, homing bump                              |
| `platformio.ini`             | Build env `mks_robin_nano_v3_1`                          |


---

## If you’re stuck

Say which **Step number** you’re on, and paste either:

- what you see on the screen, or  
- the serial reply to the last command you sent.

