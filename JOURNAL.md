---
title: SCARA 3D Printer
author: Parth Bhasin and Sujay Golla
description: A 5-axis robotic arm that can 3D Print (SCARA 3D printer) 
created_at: 2025-07-02
total_hrs: 38
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

# July 9: Working on CAD Files
## Hours Spent: 8

Today, we started working on the CAD files for our printer. We made accounts for Onshape. The reason we chose Onshape is because it allows real-time collaboration online, which is a great feature for people working in teams, and it is also one of the easiest softwares for beginners. We spent a couple hours familiarizing ourselves with the software by looking at online tutorials and creating mini-projects on Onshape. Then we started discussing about our 3D printer. We narrowed down a couple features for the 3D printer, like deciding between whether we want to split the load by adding another motor and using a smaller gearbox for each or use one stepper motor with a large gearbox. We also discussed if we want to use screws to join the parts or make snap-fit joints. I then tried to make the CAD file for the base but soon realized I needed to learn a lot more before I could actually make the base :( so I went back to the drawing board. Began watching different tutorials about CAD and robotic arms and made a couple more mini projects. Now, I first want to create a list of parts and think about how they will all fit together before diving straight into designing the base. Hopefully I can make the actual base tomorrow :) !

PS: No GitHub links for today because we did not actually commit anything to Git today, it was more of research and learnings!

# July 16: 3D Printed Sections list + CAD
## Hours Spent: 6

Today, we came up with a list of parts that need to be designed on Onshape while delving deeper into the structure and function of every component of the robotic arm that we took inspiration from. After hours of narrowing things down and coming up with different ideas, we made an ordered list from the shoulder/base of the arm to the tip:
<img width="652" height="1004" alt="image" src="https://github.com/user-attachments/assets/9eca806d-0c10-41fe-884f-11ca8562677b" />

We hope that this table will help us stay organized and not procrastinate on the CAD any further :D
We decided to split the work and make each person start from different ends of the list, so we made progress on the first and last parts from the list.

The last part looks like this:
<img width="673" height="761" alt="image" src="https://github.com/user-attachments/assets/4164249b-9373-41ad-9980-fcab98f73b9a" />

The first part looks like this so far:
<img width="1090" height="943" alt="image" src="https://github.com/user-attachments/assets/0a69ef89-cded-4019-9612-1e3c3aef6150" />

We plan to spend more time and finish the CAD asap. While we are heavily inspired by the tutorial, we are referencing it for the dimensions of bolts and general dimensions of the arm, just so we can go off of something. The actual arm will look different and of course, the functionality will be much more complex and unique. 

# July 17: CAD + BOM
## Hours Spent: 5

Today, we made progress on the CAD from the wrist of the arm. We spent a lot of time working on the wrong idea of finding a way to install the rollers from the extruder kit, and after designing the next part for a few hours, we realized we could just directly connect it to the "Wrist Pitch End." Then, we fixed the CAD and realized the next part needed precise details about the motor. However, we also realized the delivery date for AliExpress is going past the event, so we had to find new motors and gearboxes, which we did luckily! It also saved us in AliExpress shipping costs so that was a bonus! So, the part from the tip of the arm looks like this now: 
<img width="1422" height="1023" alt="image" src="https://github.com/user-attachments/assets/bea4c654-e2fb-4fac-b383-1ea5b1491aab" />

The part that we also made on progress looks like this (just need to design a section to fit the motor + gearbox and ensure it connects to the next part, which should hopefully be quick for tomorrow:
<img width="1170" height="1069" alt="image" src="https://github.com/user-attachments/assets/51847805-71f8-4f99-8f1c-dc297a0b86fe" />

The BOM looks like this now:
<img width="1865" height="1050" alt="image" src="https://github.com/user-attachments/assets/ddea0c67-2619-4a7c-8a7b-030e967b4d83" />

Tomorrow, hopefully we can make more progress from the lessons learned today ToT

# July 18: CAD
## Hours Spent: 6

We continued to make progress in both directions. From the wrist end of the arm, we modified and finished on a couple of parts, finishing the wrist section of the arm, and made progress on the forearm. 
<img width="1020" height="880" alt="image" src="https://github.com/user-attachments/assets/93590982-1fa2-4cc1-a5c6-19ca3f460b23" />
<img width="1002" height="1088" alt="image" src="https://github.com/user-attachments/assets/d284d135-8772-4c2d-928a-d8eba7778aad" />
<img width="771" height="591" alt="image" src="https://github.com/user-attachments/assets/08ebc11a-22a7-4ba5-8073-92a2654ed647" />
<img width="593" height="819" alt="image" src="https://github.com/user-attachments/assets/177370f7-608a-445c-a424-31a615b23238" />
<img width="1058" height="948" alt="image" src="https://github.com/user-attachments/assets/ae786139-1d8d-40c0-afde-78cc67402dc8" />
<img width="689" height="430" alt="image" src="https://github.com/user-attachments/assets/9fc436db-c0f9-4d16-bba8-531e15eb1b4a" />

Just plan to continue making progress from both ends!
