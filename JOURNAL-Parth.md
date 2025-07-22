---
title: DUM-E Printer (A SCARA 3D Printer)
author: Parth Bhasin
description: A 5-axis robotic arm that can 3D Print (SCARA 3D printer) 
created_at: 2025-07-02
total_hrs: 139
---

# July 1: Brainstorming
## Hours Spent: 4
After multiple options were discussed, me and my partner (Sujay Golla) decided to build a SCARA 3D printer. We discussed what features we want our 3D printer to have and looked for inspiration from other 3D Printers.

A feature I want to include:
- Info display screen (temperature, progress, etc.)

# July 3: Reading Tutorials
## Hours Spent: 10

I browsed the internet to find all the 3D printer or robotic arm tutorials I could find. I also used Hackclub highway 3D printer guides. I watched/read tutorials basically to understand the project better. 
I started working on the BOM to get a better idea of the dimensions of the parts and electronics to start working on the wiring diagrams and the CAD. We referred to the following tutorials to get a better sense of how our printer will work:
- https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html
- https://roboticworx.io/blogs/projects/build-a-5-axis-industrial-grade-robotic-arm-that-learns-how-to

Then, we came up with a rough idea for the BOM:
- We can't decide between Servos or stepper motors yet
- Belt, pulley wheels, bearings, wires, jumper wires
- Motherboard (preferably with Marlin 2.0)
- Extruder stuff
- Power supply
- Filament (for the 3D printed shell of the arm)

We plan to finish the BOM together while working on wiring diagrams and CAD simultaneously to make sure we include all of the components needed to make the project.

Here is the first page of tutorials doc I made:
<img width="537" height="504" alt="image" src="https://github.com/user-attachments/assets/cc8eba26-1dae-4b32-a49b-7d4cb635758c" />


# July 7: Working on BOM and the wiring diagram
## Hours Spent: 8
Today, we worked on finalizing our BOM by sourcing parts from AliExpress and Amazon (wherever they are cheaper) by referencing the same tutorials, picking all the smaller items like wires and tools. I sourced half the parts and my teammate did the rest. For now, our BOM looks like:
![image](https://github.com/user-attachments/assets/85b6ffa2-705f-4dd9-9569-538b139e3fe4)

Hopefully, we can get designing in a few days!

# July 9: Starting to make CAD Files
## Hours Spent: 8

Today, I started working on the CAD files for our printer. I made accounts for Onshape. The reason I chose Onshape is because it allows real-time collaboration online, which is a great feature for people working in teams, and it is also one of the easiest softwares for beginners. I spent a couple hours familiarizing myself with the software by looking at online tutorials and creating mini-projects on Onshape. Then we started discussing about our 3D printer. We narrowed down a couple features for the 3D printer, like deciding between whether we want to split the load by adding another motor and using a smaller gearbox for each or use one stepper motor with a large gearbox. We also discussed if we want to use screws to join the parts or make snap-fit joints. I want to learn more about Onshape and create a list of parts and think about how they will all fit together before diving straight into designing the printer.

# July 10-15: Learning Onshape
## Hours Spent: 18

I tried to start working on the printer but ran into a lot of issues mainly because we had never used Onshape and weren't familiar with the features and tools. I spent a few days explore different tools and creating mini projects on Onshape. I didn't get started on the actual printer because of some other personal commitments.


# July 16: 3D Printed Sections list + CAD
## Hours Spent: 12

Today, I actually started designing! I created the base plate using circle sketches and extrusions. I am really enjoying working with Onshape!
The first part looks like this so far:
<img width="1090" height="943" alt="image" src="https://github.com/user-attachments/assets/0a69ef89-cded-4019-9612-1e3c3aef6150" />

Me and my teammate decided to start from the opposite ends. So, I am working on the Base and working my way upwards while he startes from te top and works downward. However, the Base plate and the Base are both complex parts so let's see how many parts I can actually end up making. Moreover, while we are inspired by the tutorial, we are referencing it for the dimensions of bolts and general dimensions of the arm, just so we can go off of something. The actual arm will look different and of course, the functionality will be much more complex and unique. 

# July 17: CAD + BOM
## Hours Spent: 5

Continued working on the base plate. Learnt a bunch of new features. Most importantly, I leart how to sketch on a curved surface which was kinda tricky for a beginner like me.

<img width="822" height="680" alt="image" src="https://github.com/user-attachments/assets/22ec5293-cd29-4f58-bbb1-067fc9ce33e3" />


The BOM looks like this now:
<img width="1865" height="1050" alt="image" src="https://github.com/user-attachments/assets/ddea0c67-2619-4a7c-8a7b-030e967b4d83" />

# July 18: CAD
## Hours Spent: 11

Continued working on the base plate. This is how it currently looks:
<img width="1104" height="647" alt="image" src="https://github.com/user-attachments/assets/dbef634c-a121-4ecb-9c2f-0f709caefc96" />

Learnt to use the circular pattern tool!


# July 19: CAD
## Hours Spent: 12

I started working on the base today. It was so frustrating to make the ridges and I had to make it in 5 different draft files before it finally worked. However, my partner and I made a lot of progress in the CAD today, possibly over 70% done the entire arm. From the wrist end of the arm, we finished the entirety of J2 and worked on 70% of J1. A lot of parts for J1 are going to be similar to J2, so we hope this will be finished even quicker.

One of the errors I could not fix for a long time:

<img width="864" height="736" alt="image" src="https://github.com/user-attachments/assets/ed282311-ebbf-48ea-a79d-b6cd41c78362" />

But then I fixed it:

<img width="1035" height="770" alt="image" src="https://github.com/user-attachments/assets/6e3c5cfa-4d2f-4d2d-b9ec-a1f8f3ee2515" />

And then I circle patterned it:

<img width="1346" height="614" alt="image" src="https://github.com/user-attachments/assets/618e4583-577a-43f2-a2d9-1b41176a3bad" />

And it finally works:

<img width="610" height="445" alt="image" src="https://github.com/user-attachments/assets/d303b736-2586-4a04-af79-8e735548405c" />


# July 20: CAD
## Hours Spent: 14

I panicked today because I realized that AliExpress might take too much time to ship the parts and wanted to submit today. I and my teammate decided to lock in and we finished designing all the parts. Then we started assembling all the parts in the assembly file. There were so many errors and dimensions issues that we had to go back and redo a bunch of parts. I fixed the J1 Base file that my teammate made because for some reason, the holes for the screws weren't aligned properly. The entire process took way longer than we expected and we had to pull an all-nighter. Unfortunately we could not submit because we still had a bunch of stuff left to do. We must submit this tomorrow tho!

<img width="627" height="770" alt="image" src="https://github.com/user-attachments/assets/6d315f8f-133c-4e63-a437-6d69c2af0e0a" />



# July 21: CAD
## Hours Spent: 14

We finished assembling most of the parts. Next, we had to add a bunch of makeshift parts in the assembly file. These included the bearings, motors, screen, power source, motherboard etc. Basically, these are the parts we are not going to 3D print, but instead buy. For instance, we would buy the motors, not 3D print the motors. But, in order to be 100% precise in the assembly file, we created makeshift designs for all these parts so that the dimensions make sense in the assembly. I personally made the makeshift bearing, makeshift screen and one of the makeshift motors. This was an interesting process because I learnt a few new tools like the Boolean, Union, Split and Transform tools. I designed a rough sketch for the extruder and added that to the assembly file for accuracy. Then my teammate found an open-source file for a SCARA 3D Printer's firmware which we decided to use as the template for our printer too. The firmware is going to be essentially the same because it is also a SCARA printer and uses the same SCARA kinematics. We will configure the firmware specific to our robot arm once we get the parts. Then, we made a ReadMe file for our printer and now we are finally ready to submit!

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
