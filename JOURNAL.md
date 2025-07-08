---
title: SCARA 3D Printer
author: Parth Bhasin and Sujay Golla
description: A 5-axis robotic arm that can 3D Print (SCARA 3D printer) 
created_at: 2025-07-02
total_hrs: 13
---

# July 1: Brainstorming
## Hours Spent: 2
We decided to build a SCARA 3D printer from various different options. We discussed what features we want our 3D printer to have and looked for inspiration from other 3D Printers.

Some features we want to include:
- 5 DOF Arm with a 3D printed case
- Some configuration of an extruder
- Info display screen (temperature, progress, etc.)

# July 3: Working on BOM
## Hours Spent: 3
We decided to start working on the BOM to get a better idea of the dimensions of the parts and electronics to start working on the wiring diagrams and the CAD. We referred to the following tutorials to get a better sense of how our printer will work:
- https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html
- https://roboticworx.io/blogs/projects/build-a-5-axis-industrial-grade-robotic-arm-that-learns-how-to

Then, we came up with a rough idea for the BOM:
- Servos or stepper motors????
- Belt, pulley wheels, bearings, wires, jumper wires
- Motherboard (preferably with Marlin 2.0)
- Extruder stuff
- Power supply
- Filament (for the 3D printed shell of the arm)

We also started gathering links for some of the major expenses and parts for a proper BOM:
![image](https://github.com/user-attachments/assets/7395b70e-a7b5-4fa7-b740-357efa314767)

We plan to finish the BOM while working on wiring diagrams and CAD simultaneously to make sure we include all of the components needed to make the project.

# July 7: Working on BOM and the wiring diagram
## Hours Spent: 8
Today, we worked on finalizing our BOM by sourcing parts from AliExpress and Amazon (wherever they are cheaper) by referencing the same tutorials, picking all the smaller items like wires and tools. AliExpress' welcome offer helped cut down costs, but some parts require paid shipping, which might take away the benefit of buying for cheap from AliExpress. Finding the cheapest options, understanding the purpose and optimizing the models for different parts took a lot of time, especially as we are new to hardware projects. For now, our BOM looks like:
![image](https://github.com/user-attachments/assets/85b6ffa2-705f-4dd9-9569-538b139e3fe4)

Picking the stepper motors and the gearboxes was the most tiring task of all. We had to estimate lengths and weights to calculate torques on the arm to pick the right gearboxes:
![image](https://github.com/user-attachments/assets/b4a454e1-e8d1-455a-9c47-4499e5d3bd40)

We also made a wiring diagram for the printer motherboard, but since we don't have much experience with professional tools, we made a comprehensive diagram on Canva:
![image](https://github.com/user-attachments/assets/70800945-6428-4a2c-b3ad-611858795715)

With all of the specifications for the parts, we can finally work on the CAD starting tomorrow!
