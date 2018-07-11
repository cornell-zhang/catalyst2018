
Rapid Targeting System
---

### Goal
---
Use the robot to navigate a maze using various sensors. We will have a competition between groups to see which robot can navigate the maze the fastest. You are allow to use all sensors installed on the robot and program them to aid your progress.

### The obstacle
---
The maze is a square covered all all sides with a wooden wall and has a single wooden wall that extends halfway through the middle of the maze. The floor of the maze is entirely wood except for an all black square that signifies the target location. The wood all have same color. The robot will start at a randomly chosen position in opposite side of the wall from the target and will need to spin around for a random degree and then navigate the maze.

We may add more obstacles to the course in order to test the robustness of your robot intelligence.

### Robot specification
---
The robot have a few updates in comparison to lab 2. We have added a wifi shield to allow us to communicate with the robot using Digitrec from lab 3. Follow the tutorial in the folder titled "Communications Tutorial" in order to upgrade your robot. You will need to use the wifi shield to program the robot to spin initially when we draw a number on Digitrec.   

### Tasks
--- 
- Program the wifi shield on the robot to allow it to receive information from the Digitrec website.
- Spin the robot based on the number drawn on the Digitrec website.
- Have the robot navigate the maze in shortest possible time.
- Make sure the robot's intelligence is robust enough that it can handle different maze configurations.

### Design tips
---
- To help improve navigation time, you can increase the speed of the motors so that the robot can move and turn faster. However, the robot will be less stable and likely tip over. You will therefore need to improve stability.
- There are two infrared sensors on the robot. One on the front and one on the bottom; the bottom can help detect the target and the front can be used to sense distance between the sensor and the wall. It is recommended that you utilize the front infrared sensor to allow the robot to see the distance between itself and the wall; think about how the robot will know (or can guess) that it is going the right way. The front infrared sensor can also prevent the robot from getting stuck.
- The bumpers are an excellent tool to provide information to the robot. Look at the extensions for lab 2 where you implement the bumper to allow the robot to intelligently turn based on which bumper is pressed.


### Programming tips
---


