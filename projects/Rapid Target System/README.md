
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
The robot have a few updates in comparison to lab 2. We have added a wifi shield to allow us to communicate with the robot using Digitrec from lab 3. You will need to use the wifi shield to program the robot to spin initially when we draw a number on Digitrec. To utilize the wifi shield, some modifications to the wiring of the robot are needed. Follow the tutorial in the folder titled "Communications Tutorial" in order to upgrade your robot. We also have access to the front facing infrared sensor.    

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
- The bumpers are an excellent tool to provide information to the robot. Look at the extensions for lab 2 where you implement the bumper to allow the robot to intelligently turn based on which bumper was pressed. 


### Programming tips
---
As in lab 2, you will be programming in C++ on the Arduino IDE. You will also verify and upload the code using the IDE.
Even though you will use code from lab 2, you will likely find yourself writing more lines code to configure the robot AI. It is therefore very useful to develop good coding practices and tricks in order to organize your code and improve the readability of your code.

### Comments:
Since you will be working in a group with other students, comments are a very good way to tell others what your code does as well as help group members debug the code. In C++, comments can be made using ```//```, which comments lines, or ```/*..*/```, which comments a block. 
Uses for comments:
- You can comment out code in order to help isolate bugs. 
- Label variables and functions
- Insert comments next to lines of code to tell the user what that line does.
- Put instructions on how to use this code/program.


### Functions:
Functions are a group of statements that perform a specific task. Function are useful for performing repetitive tasks.
Declare a function like this:
```return_type function_name( parameter ) {
   body of the function
}
```
Example:
```void robot_turn(int direction){
		Serial.print(direction);
}```
In the above example, ```void``` means that the doesn't return anything. ```robot_turn``` is the function name. The parameter is specified the same way as the function with a type and name. The function takes in an integer as a parameter and prints it out to the Serial monitor. 





