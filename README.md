# DUM-E Printer
## The Inspiration
We wanted to build our own 3D printer. Being die-hard Tony Stark fans, we decided to make a SCARA-style 3D printer. Introducing DUM-E Printer! It is a 5-axis robotic arm with with an extruder attached to the end to 3D print. Jokes aside, this project is really useful, becuase unlike the conventional fusion printers, the SCARA (Selective Compliance Assembly Robotic Arm) style printer is not limited by the volume of the printer bed. Morevoer, it's a lot more precise and offers greater flexibility because it has 5 axes of rotation and can directly print on top of any surface. Most importantly, SCARA-style printers are really expensive with almost no options for hobbyists. The only SCARA printers we could find were for industry and not amateurs, thus we took it as a challenge to make one and possess this cool Tony Stark-style tech.

## The Struggle
This was an extremely challenging process partly because there is no tutorial to make a SCARA 3D printer. We used a bunch of tutorials as references [in-text citation] to make a robotic arm and then figured out a way to add the 3D printer extruder to it. It's safe to say that in the past 3 weeks, 2 amateurs have become Onshape pros.

## Technical Features
We plan on using an affordable prebuilt extruder from Creality to do the actual printing. The Marlin firmware is run by an Mks Robin Nano Motherboard. For the printer's display, we have a TS35 Touchscreen. DUM-E Printer uses 5 Stepper Motors to achieve motion. There are multiple bearings in the joints to facilitate rotation.

## CAD Model
Isometric view of the assembled printer:

<img width="499" height="610" alt="image" src="https://github.com/user-attachments/assets/9ae98a20-3794-44c8-b39b-953e41bf6d19" />

Top view of the assembled printer:

<img width="310" height="695" alt="image" src="https://github.com/user-attachments/assets/bafcc168-3faf-4f0e-9575-918b13069217" />

Front view of the assembled printer:

<img width="248" height="685" alt="image" src="https://github.com/user-attachments/assets/c6dd499b-586e-4841-9b29-13f030f3f169" />

Side view of the assembled printer:

<img width="662" height="666" alt="image" src="https://github.com/user-attachments/assets/44d2b13b-2851-4779-b700-ebcbfb8c47e9" />

Exploded Diagram of the printer (to view the motors and the bearings):

<img width="379" height="704" alt="image" src="https://github.com/user-attachments/assets/4cc959fd-b1a6-4b19-b93b-f2d8bf9f4766" />

<img width="216" height="626" alt="image" src="https://github.com/user-attachments/assets/9a663953-a13c-495b-8712-df441ea6aa9b" />


Note: The blue parts are the ones that need to be 3D printed and the grey ones are the makeshift components

## Wiring Diagram
<img width="878" height="592" alt="image" src="https://github.com/user-attachments/assets/e750bcd7-6ea8-4e28-a9ea-e4199738012b" />

## BOM
Note: We used Amazon for some of the parts because they were either the same price or cheaper than Aliexpress. Amazon's delivery is much faster than Aliexpress so we preferred to use it if the price is same or less. All the costs beyond $350 USD will be covered by Sujay and Parth.
| Part Name | Quantity | CAD Unit Price | USD Unit Price | USD Total Cost | Link |
|---|---|---|---|---|---|
| MEISHILE 24V 25A 600W Switching Power Supply | 1 | $40.99 | $29.92 | $29.92 | [Link](https://www.amazon.ca/MEISHILE-Switching-Transformer-Converter-Amplifier/dp/B0C299DG1H) |
| Creality Ender 3 Direct Drive Extruder Upgrade Kit | 1 | $41.39 | $30.21 | $30.21 | [Link](https://www.amazon.ca/Official-Creality-Extruder-Compatible-3D/dp/B0C2CH7P54) |
| Mks Robin Nano V3.1 Eagle 32bit Control Panel TMC2209 with Screen | 1 | $52.99 | $38.68 | $38.68 | [Link](https://www.aliexpress.com/item/1005008555474559.html) |
| 22 AWG 10 m shielded wire | 1 | $9.58 | $6.99 | $6.99 | [Link](https://www.aliexpress.com/item/4000850790419.html) |
| 22 AWG 20 m silicone wire | 1 | $8.19 | $5.98 | $5.98 | [Link](https://www.aliexpress.com/item/1005006250522147.html) |
| Crimper Cable Cutter Adjustable Automatic Wire Stripper | 1 | $8.39 | $6.12 | $6.12 | [Link](https://www.aliexpress.com/item/1005007148577702.html) |
| 10PCS PCB Terminal Block Connector | 1 | $1.61 | $1.18 | $1.18 | [Link](https://www.aliexpress.com/item/1005006642865467.html) |
| 200Pcs/Box 2.54mm Pitch JST SM/Dupont Jumper Wire Connector Kit | 1 | $7.39 | $5.39 | $5.39 | [Link](https://www.aliexpress.com/item/1005003140788241.html) |
| M3 M4 M5 Bolt kit | 1 | $23.79 | $17.37 | $17.37 | [Link](https://www.aliexpress.com/item/1005008261719970.html) |
| 4x10x4 mm Bearings Set of 10 | 1 | $5.79 | $4.23 | $4.23 | [Link](https://www.aliexpress.com/item/1005007668446060.html) |
| 18x30x7 mm Bearings Set of 10 | 1 | $11.89 | $8.68 | $8.68 | [Link](https://www.aliexpress.com/item/1005009272681515.html) |
| Bore with teeth set of 6 | 1 | $8.51 | $6.21 | $6.21 | [Link](https://www.aliexpress.com/item/1005007557987612.html) |
| Belt 6mm 5m open | 1 | $5.32 | $3.88 | $3.88 | [Link](https://www.aliexpress.com/item/1005007542222728.html) |
| Bore without teeth set of 6 | 1 | $8.60 | $6.28 | $6.28 | [Link](https://www.aliexpress.com/item/1005007557987612.html) |
| Digital Caliper | 1 | $7.25 | $5.29 | $5.29 | [Link](https://www.aliexpress.com/item/1005003772701402.html) |
| Nema23 1.5 Nm stepper motors | 2 | $41.38 | $30.21 | $60.41 | [Link](https://www.aliexpress.com/item/1005007638437234.html) |
| 14:1 Gearbox + Stepper motor | 1 | $34.58 | $25.24 | $25.24 | [Link](https://www.aliexpress.com/item/1005007401751232.html) |
| 19:1 Gearbox + Stepper motor | 1 | $34.58 | $25.24 | $25.24 | [Link](https://www.aliexpress.com/item/1005007401751232.html) |
| 51:1 Gearbox + Stepper motor | 1 | $35.58 | $25.97 | $25.97 | [Link](https://www.aliexpress.com/item/1005007401751232.html) |

Total cost after taxes (in USD) = $354.03

## Citations
https://roboticworx.io/blogs/projects/build-a-5-axis-industrial-grade-robotic-arm-that-learns-how-to
https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html
https://grabcad.com/library/nema-17-40mm-stepper-motor-1
https://www.thingiverse.com/thing:2703913#google_vignette
https://ceadgroup.com/?gad_source=1&gad_campaignid=16706268843&gbraid=0AAAAADluaE2qMilXf5DGrwfPtwiKrZWuE&gclid=Cj0KCQjw64jDBhDXARIsABkk8J6YH5XEkbH4B8oL-57sFGOkRXjcGaRCpnTnYhE8oyMMPhciKx2Tg00aAlF1EALw_wcB
https://www.3dwasp.com/en/extruders-for-robotic-arm/?utm_term=&utm_campaign=%5BSV%5D+P-Max+-+Cerebro+-+EN&utm_source=adwords&utm_medium=ppc&hsa_acc=3352968755&hsa_cam=22610030082&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=22619977153&gbraid=0AAAAADi5FmbN5TTzwj0dd_AGEi3CcjKtL&gclid=Cj0KCQjw64jDBhDXARIsABkk8J5z179wIPrNsbFpnReQB0n60VD38eaT0RRxBTg0PEWfnaxmk3edToUaArlMEALw_wcB
https://www.youtube.com/watch?v=5toNqaGsGYs
https://www.youtube.com/watch?v=OiQKw0lZ5Rw

## Quick Notes from Authors
1. We made makeshift files and got some pre-made files for motors, gearboxes, etc. that are not going to be 3D printed as placeholders to make sure all of our CAD files are formatted properly
2. We found a template for the Marlin firmware that corresponds to the kinematics of a SCARA 3D Printer, so we plan to use that as a template and configure it based on our arm as we build it physically. 
