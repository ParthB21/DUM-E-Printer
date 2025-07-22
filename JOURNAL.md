---
title: DUM-E Printer (A SCARA 3D Printer)
authors: Parth Bhasin and Sujay Golla
description: A 5-axis robotic arm that can 3D Print (SCARA 3D printer) 
created_at: 2025-07-02
total_hrs: 139
---

# July 1: Brainstorming
## Hours Spent: 5
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

# July 9: Starting to make CAD Files
## Hours Spent: 8

Today, we started working on the CAD files for our printer. We made accounts for Onshape. The reason we chose Onshape is because it allows real-time collaboration online, which is a great feature for people working in teams, and it is also one of the easiest softwares for beginners. We spent a couple hours familiarizing ourselves with the software by looking at online tutorials and creating mini-projects on Onshape. Then we started discussing about our 3D printer. We narrowed down a couple features for the 3D printer, like deciding between whether we want to split the load by adding another motor and using a smaller gearbox for each or use one stepper motor with a large gearbox. We also discussed if we want to use screws to join the parts or make snap-fit joints. We want to learn more about Onshape and create a list of parts and think about how they will all fit together before diving straight into designing the printer.

# July 10-15: Learning Onshape
## Hours Spent: 18

We tried to start working on the printer but ran into a lot of issues mainly because we had never used Onshape and weren't familiar with the features and tools. We spent a few days explore different tools and creating mini projects on Onshape. We didn't get started on the actual printer because of some other personal commitments.


# July 16: 3D Printed Sections list + CAD
## Hours Spent: 12

Today, we came up with a list of parts that need to be designed on Onshape while delving deeper into the structure and function of every component of the robotic arm that we took inspiration from. After hours of narrowing things down and coming up with different ideas, we made an ordered list from the shoulder/base of the arm to the tip:
<img width="652" height="1004" alt="image" src="https://github.com/user-attachments/assets/9eca806d-0c10-41fe-884f-11ca8562677b" />

We hope that this table will help us stay organized and not procrastinate on the CAD any further :D
We decided to split the work and make each person start from different ends of the list, so we made progress on the first and last parts from the list.

The last part looks like this:
<img width="673" height="761" alt="image" src="https://github.com/user-attachments/assets/4164249b-9373-41ad-9980-fcab98f73b9a" />

The first part looks like this so far:
<img width="1090" height="943" alt="image" src="https://github.com/user-attachments/assets/0a69ef89-cded-4019-9612-1e3c3aef6150" />

We plan to spend more time and finish the CAD asap. While we are inspired by the tutorial, we are referencing it for the dimensions of bolts and general dimensions of the arm, just so we can go off of something. The actual arm will look different and of course, the functionality will be much more complex and unique. 

# July 17: CAD + BOM
## Hours Spent: 10

Today, we made progress on the CAD from the wrist of the arm. We spent a lot of time working on the wrong idea of finding a way to install the rollers from the extruder kit, and after designing the next part for a few hours, we realized we could just directly connect it to the "Wrist Pitch End." Then, we fixed the CAD and realized the next part needed precise details about the motor. However, we also realized the delivery date for AliExpress is going past the event, so we had to find new motors and gearboxes, which we did luckily! It also saved us in AliExpress shipping costs so that was a bonus! So, the part from the tip of the arm looks like this now: 
<img width="1422" height="1023" alt="image" src="https://github.com/user-attachments/assets/bea4c654-e2fb-4fac-b383-1ea5b1491aab" />

The part that we also made on progress looks like this (just need to design a section to fit the motor + gearbox and ensure it connects to the next part, which should hopefully be quick for tomorrow:
<img width="1170" height="1069" alt="image" src="https://github.com/user-attachments/assets/51847805-71f8-4f99-8f1c-dc297a0b86fe" />

The BOM looks like this now:
<img width="1865" height="1050" alt="image" src="https://github.com/user-attachments/assets/ddea0c67-2619-4a7c-8a7b-030e967b4d83" />

Tomorrow, hopefully we can make more progress from the lessons learned today ToT

# July 18: CAD
## Hours Spent: 11

We continued to make progress in both directions. From the wrist end of the arm, we modified and finished on a couple of parts, finishing the wrist section of the arm, and made progress on the forearm. 
<img width="1020" height="880" alt="image" src="https://github.com/user-attachments/assets/93590982-1fa2-4cc1-a5c6-19ca3f460b23" />
<img width="1002" height="1088" alt="image" src="https://github.com/user-attachments/assets/d284d135-8772-4c2d-928a-d8eba7778aad" />
<img width="771" height="591" alt="image" src="https://github.com/user-attachments/assets/08ebc11a-22a7-4ba5-8073-92a2654ed647" />
<img width="593" height="819" alt="image" src="https://github.com/user-attachments/assets/177370f7-608a-445c-a424-31a615b23238" />
<img width="1058" height="948" alt="image" src="https://github.com/user-attachments/assets/ae786139-1d8d-40c0-afde-78cc67402dc8" />
<img width="689" height="430" alt="image" src="https://github.com/user-attachments/assets/9fc436db-c0f9-4d16-bba8-531e15eb1b4a" />

Just plan to continue making progress from both ends!

# July 19: CAD
## Hours Spent: 12

We made a lot of progress in the CAD today, possibly over 70% done the entire arm. From the wrist end of the arm, we finished the entirety of J2 and worked on 70% of J1. A lot of parts for J1 are going to be similar to J2, so we hope this will be finished even quicker. The biggest challenge was trying to find a way to create ridges for our timing belts. This took a lot of trial and error, but after hours of work, we figured it out and made it for the J2 components. Here are some parts we worked on and finished today: 
<img width="680" height="1123" alt="image" src="https://github.com/user-attachments/assets/df847533-d002-4cc0-9bf2-b043ddd52704" />
<img width="1240" height="1100" alt="image" src="https://github.com/user-attachments/assets/d92f0324-77ab-4ef2-9807-54ddb33befb7" />
<img width="495" height="1165" alt="image" src="https://github.com/user-attachments/assets/5c373941-7c2a-423d-b952-a424f3239fdd" />
<img width="712" height="1176" alt="image" src="https://github.com/user-attachments/assets/b0fa24f7-2344-447d-92eb-c3cc1f19dee3" />

Tomorrow, we plan to finish the CAD and submit the proposal!

# July 20: CAD
## Hours Spent: 28

You might be wondering how we spent more than 24 hours in a day. Well, we are a team of 2 and we both worked for 14 hours each (we were on call working together the entire day) so it was 20 man-hours. The reason we were so locked in was because we kinda panicked thinking that AliExpress might take too much time to ship the parts and wanted to submit today. Anyways, we finished designing all the parts. Then we started assembling all the parts in the assembly file. There were so many errors and dimensions issues that we had to go back and redo a bunch of parts. The entire process took way longer than we expected and we had to pull an all-nighter. Unfortunately we could not submit because we still had a bunch of stuff left to do. We must submit this tomorrow!

<img width="627" height="770" alt="image" src="https://github.com/user-attachments/assets/6d315f8f-133c-4e63-a437-6d69c2af0e0a" />



# July 21: CAD
## Hours Spent: 24

Same as the previous day, we worked together and our combined time was 24 hours. We finished assembling most of the parts. Next, we had to add a bunch of makeshift parts in the assembly file. These included the bearings, motors, screen, power source, motherboard etc. Basically, these are the parts we are not going to 3D print, but instead buy. For instance, we would buy the motors, not 3D print the motors. But, in order to be 100% precise in the assembly file, we created makeshift designs for all these parts so that the dimensions make sense in the assembly. Moreover, some parts, like the motherboard were too time-consuming and complex, so we just created a cuboid with the max volume to represent the motherboard, obviously we're gonna buy the motherboard, not 3D print it, the design in the assembly file is just for representation. We designed a rough sketch for the extruder and added that to the assembly file for accuracy. Then we found an open-source for a SCARA 3D Printer's firmware which we decided to use as the template for our printer too. The firmware is going to be essentially the same because it is also a SCARA printer and uses the same SCARA kinematics. We will configure the firmware specific to our robot arm once we get the parts. Then, we made a ReadMe file for our printer and now we are finally ready to submit!

Front view of the assembled printer:
<br> <img width="444" height="681" alt="image" src="https://github.com/user-attachments/assets/20f53289-2f48-491e-8a1f-919dd3309fdf" /> <br>

Side view of the assembled printer:
<br> <img width="644" height="702" alt="image" src="https://github.com/user-attachments/assets/b986159e-1a02-4279-8913-f03baa6715e2" />
<br>
Isometric view of the assembled printer:
<br> <img width="301" height="590" alt="image" src="https://github.com/user-attachments/assets/3d18f342-9ec8-4660-b4f4-0ac8cf4a177a" />
<br>
Design for the spool:
<br> <img width="226" height="260" alt="image" src="https://github.com/user-attachments/assets/61266960-9136-4032-99cb-9a5578addba6" />
<br>
Design for the makeshift screen:
<br> <img width="402" height="331" alt="image" src="https://github.com/user-attachments/assets/c6c9d468-e556-4908-af3e-ece1a2a303fc" />
<br>
Updated Base Plate with the mount for the screen:
<br> <img width="712" height="501" alt="image" src="https://github.com/user-attachments/assets/d1a8bc15-a49f-456d-bfce-4eb02dd022da" />
<br>
Isometric view of the Makeshift Extruder:
<br> <img width="568" height="517" alt="image" src="https://github.com/user-attachments/assets/3676b9bf-805e-4167-babf-79662d2356d9" />
<br>
Note: We ended up changing the colors in the end to make it all 1 color, for the updated screenshots with the new colour, check the Readme file.
