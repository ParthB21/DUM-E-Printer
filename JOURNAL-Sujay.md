---
title: DUM-E Printer - Sujay's Journal
authors: Sujay Golla
description: A 5-axis robotic arm that can 3D Print (SCARA 3D printer) 
started_working: 2025-07-01
total_hrs_submitted: 80
total_hrs_worked: 89
---
(Note: we modified a few things after submission and updated the CAD files and Readme which is why the submitted hours and total hours do not match)

# July 1: Brainstorming
## Hours Spent: 5
We decided to build a SCARA 3D printer from various different options. We discussed what features we want our 3D printer to have and looked for inspiration from other 3D Printers.

Some features I wanted to include:
- 5 DOF Arm with a 3D printed case
- Some configuration of a pre-built extruder

# July 3: Working on BOM
## Hours Spent: 3
I decided to start working on the BOM to get a better idea of the dimensions of the parts and electronics to start working on the wiring diagrams and the CAD. I referred to the following tutorials to get a better sense of how our printer will work:
- https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html
- https://roboticworx.io/blogs/projects/build-a-5-axis-industrial-grade-robotic-arm-that-learns-how-to

Then, I came up with a rough idea for the BOM:
- Servos or stepper motors????
- Belt, pulley wheels, bearings, wires, jumper wires
- Motherboard (preferably with Marlin 2.0)
- Extruder stuff
- Power supply
- Filament (for the 3D printed shell of the arm)

I also started gathering links for some of the major expenses and parts for a proper BOM:
![image](https://github.com/user-attachments/assets/7395b70e-a7b5-4fa7-b740-357efa314767)

We plan to finish the BOM while working on wiring diagrams and CAD simultaneously to make sure we include all of the components needed to make the project.

# July 7: Working on BOM and the wiring diagram
## Hours Spent: 8
Today, I worked on finalizing our BOM by sourcing parts from AliExpress and Amazon (wherever they are cheaper) by referencing the same tutorials, picking all the smaller items like wires and tools. AliExpress' welcome offer helped cut down costs, but some parts require paid shipping, which might take away the benefit of buying for cheap from AliExpress. Finding the cheapest options, understanding the purpose and optimizing the models for different parts took a lot of time, especially as we are new to hardware projects. For now, our BOM looks like:
![image](https://github.com/user-attachments/assets/85b6ffa2-705f-4dd9-9569-538b139e3fe4)

Picking the stepper motors and the gearboxes was the most tiring task of all. I had to estimate lengths and weights to calculate torques on the arm to pick the right gearboxes:
![image](https://github.com/user-attachments/assets/b4a454e1-e8d1-455a-9c47-4499e5d3bd40)

I also made a wiring diagram for the printer motherboard, but since I don't have much experience with professional tools, I made a comprehensive diagram on Canva:
![image](https://github.com/user-attachments/assets/70800945-6428-4a2c-b3ad-611858795715)

With all of the specifications for the parts, we can finally work on the CAD starting tomorrow!

# July 10-15: Learning Onshape
## Hours Spent: 2

I tried to spend this time learning Onshape, but due to other commitments, I wasn't able to spend much time on it.

# July 16: 3D Printed Sections list + CAD
## Hours Spent: 12

Today, I came up with a list of parts that need to be designed on Onshape while delving deeper into the structure and function of every component of the robotic arm that I took inspiration from. After hours of narrowing things down and coming up with different ideas, I made an ordered list from the shoulder/base of the arm to the tip:
<img width="652" height="1004" alt="image" src="https://github.com/user-attachments/assets/9eca806d-0c10-41fe-884f-11ca8562677b" />

I hope that this table will help us stay organized and not procrastinate on the CAD any further :D
We decided to split the work and make each person start from different ends of the list. I started working from the last part:

The last part looks like this:
<img width="673" height="761" alt="image" src="https://github.com/user-attachments/assets/4164249b-9373-41ad-9980-fcab98f73b9a" />

I plan to spend more time and finish the CAD asap. While we are inspired by the tutorial, we are referencing it for the dimensions of bolts and general dimensions of the arm, just so we can go off of something. The actual arm will look different and of course, the functionality will be much more complex and unique. 

# July 17: CAD + BOM
## Hours Spent: 10

Today, I made progress on the CAD from the wrist of the arm. I spent a lot of time working on the wrong idea of finding a way to install the rollers from the extruder kit, and after designing the next part for a few hours, I realized we could just directly connect it to the "Wrist Pitch End." Then, I fixed the CAD and realized the next part needed precise details about the motor. However, I also realized the delivery date for AliExpress is going past the event, so I had to find new motors and gearboxes, which I did luckily! It also saved us in AliExpress shipping costs so that was a bonus! So, the part from the tip of the arm looks like this now: 
<img width="1422" height="1023" alt="image" src="https://github.com/user-attachments/assets/bea4c654-e2fb-4fac-b383-1ea5b1491aab" />

The part that I also made on progress looks like this (just need to design a section to fit the motor + gearbox and ensure it connects to the next part, which should hopefully be quick for tomorrow:
<img width="1170" height="1069" alt="image" src="https://github.com/user-attachments/assets/51847805-71f8-4f99-8f1c-dc297a0b86fe" />

The BOM looks like this now:
<img width="1865" height="1050" alt="image" src="https://github.com/user-attachments/assets/ddea0c67-2619-4a7c-8a7b-030e967b4d83" />

Tomorrow, hopefully I can make more progress from the lessons learned today ToT

# July 18: CAD
## Hours Spent: 11

We continued to make progress in both directions. From the wrist end of the arm, I modified and finished on a couple of parts, finishing the wrist section of the arm, and made progress on the forearm. 
<img width="1020" height="880" alt="image" src="https://github.com/user-attachments/assets/93590982-1fa2-4cc1-a5c6-19ca3f460b23" />
<img width="1002" height="1088" alt="image" src="https://github.com/user-attachments/assets/d284d135-8772-4c2d-928a-d8eba7778aad" />
<img width="771" height="591" alt="image" src="https://github.com/user-attachments/assets/08ebc11a-22a7-4ba5-8073-92a2654ed647" />
<img width="593" height="819" alt="image" src="https://github.com/user-attachments/assets/177370f7-608a-445c-a424-31a615b23238" />
<img width="1058" height="948" alt="image" src="https://github.com/user-attachments/assets/ae786139-1d8d-40c0-afde-78cc67402dc8" />
<img width="689" height="430" alt="image" src="https://github.com/user-attachments/assets/9fc436db-c0f9-4d16-bba8-531e15eb1b4a" />

Just plan to continue making progress from both ends!

# July 19: CAD
## Hours Spent: 12

We made a lot of progress in the CAD today, possibly over 70% done the entire arm. From the wrist end of the arm, I finished the entirety of J2 and worked on 70% of J1. A lot of parts for J1 are going to be similar to J2, so I hope this will be finished even quicker. The biggest challenge was trying to find a way to create ridges for our timing belts. This took a lot of trial and error, but after hours of work, I figured it out and made it for the J2 components. Here are some parts I worked on and finished today: 
<img width="680" height="1123" alt="image" src="https://github.com/user-attachments/assets/df847533-d002-4cc0-9bf2-b043ddd52704" />
<img width="1240" height="1100" alt="image" src="https://github.com/user-attachments/assets/d92f0324-77ab-4ef2-9807-54ddb33befb7" />
<img width="495" height="1165" alt="image" src="https://github.com/user-attachments/assets/5c373941-7c2a-423d-b952-a424f3239fdd" />
<img width="712" height="1176" alt="image" src="https://github.com/user-attachments/assets/b0fa24f7-2344-447d-92eb-c3cc1f19dee3" />

Tomorrow, we plan to finish the CAD and submit the proposal!

# July 20: CAD
## Hours Spent: 14

I continued designing from the back and finished up to J1 Base. Then we started assembling all the parts in the assembly file. There were so many errors and dimensions issues that we had to go back and redo a bunch of parts. The entire process took way longer than we expected and we had to pull an all-nighter. While Parth worked on fixing the dimensions, I worked on assembling things and arranging them in the assembly file. Unfortunately we could not submit because we still had a bunch of stuff left to do. We must submit this tomorrow!

<img width="627" height="770" alt="image" src="https://github.com/user-attachments/assets/6d315f8f-133c-4e63-a437-6d69c2af0e0a" />



# July 21: CAD
## Hours Spent: 12

We finished assembling most of the parts. I also made the spool holder. I found all the makeshift components from the tutorial's CAD assembly file and other online sources and made some of my own, like the makeshift power supply and motherboard. The makeshift parts helped in finding any errors in the dimensions of the 3D print CAD files. I made the motherboard and power supply into rectangular prisms showing its maximum occupying volume, especially as their actual designs are extremely complex and not necessary for the assembly file. Then I also found an open-source firmware config file for a SCARA 3D Printer, which we decided to use as the template for our printer too. We will configure the firmware specific to our robot arm once we get the parts. 
Then, we made the ReadMe file together and all the other small requirements, and now we are finally ready to submit!

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

# July 22 : Feedback and planning
## Hours spent : 2

After submitting our project, we got some feedback from Toby and decided to work on it asap. First, I broke down the feedback into some steps or guidelines for reference:
<img width="1121" height="372" alt="image" src="https://github.com/user-attachments/assets/a3b6617c-e3cf-42b7-86e2-62edc190741f" />

Though we realized backlash would be an issue from the start, we decided to try and minimize it after Toby's comment. Shielded wires also seemed necessary so we decided to add that. I realized I should recalculate the final torques, which I will do tomorrow. 

Tomorrow, I'll also work on part sourcing and finding alternatives and ways to cut down the budget a little so that we can potentially use better motors.

# July 23: Torques, Parts, etc.
## Hours spent: 3

Today, I calculated the torques from the masses Parth calculated. This table helps confirm that our current motors + gearboxes are capable enough to lift the arm.
<img width="1023" height="766" alt="image" src="https://github.com/user-attachments/assets/0a356698-5225-4f1d-9dc4-97194a5f34a2" />

But, to avoid backlash and compounding error, we had to eliminate as many gearboxes as possible, so we found Nema23 alternatives for the wrist section of the arm. Even if we wanted to remove gearboxes for the others, we couldn't as the gearboxes would still be needed but at least we tried reducing backlash should hopefully that counts for something. I also realized we could cut filament from the budget as I have some 3D pen filament that could be used for testing and save some money there. Here's some parts I found today (but that haven't been added to the BOM):
<img width="981" height="897" alt="image" src="https://github.com/user-attachments/assets/bc9e14be-8e3a-457c-ae28-882922d9bf29" />

We will update the CAD tmrw and hopefully resubmit everything soon.

# July 24: CAD
## Hours spent: 1

Today, we changed the sizes for the motor compartments in the wrist section and update the sizes for the screw holes. I worked on Wrist Pitch Mount while Parth worked on Wrist Roll. Here's what I ended up making:
<img width="1316" height="976" alt="image" src="https://github.com/user-attachments/assets/4ae402c6-7b75-4a86-9ae7-fb1dd1f68717" />

I also realized there were issues with the motor horn for the Wrist Pitch, so I decided to fix those tomorrow.

# July 25: CAD and updating Github
## Hours spent: 3

Today, I decided to finish the assembly file, group all the components in their final positions together and make sure everything was aligned to polish it. I also added the new Nema23 motors to the assembly.  
<img width="836" height="1076" alt="image" src="https://github.com/user-attachments/assets/21bf2b2c-622a-455d-b704-6971f691d547" />

I also fixed the Wrist Pitch section by recreating the Wrist Pitch End
<img width="1079" height="1041" alt="image" src="https://github.com/user-attachments/assets/898f1d17-18f4-446e-8135-674a7695ba95" />

I finalized the BOM and uploaded it to Github. To reply to Toby, I will further explain the belt mechanism, how theres a gap for double layering and increasing the tension. I will talk about ways plan to connect the wires, by sending them through some of the extra holes we made throughout the arm and using adhesive cable ties to make sure they're all in place. With this final update, we should hopefully be ready to get approved.
