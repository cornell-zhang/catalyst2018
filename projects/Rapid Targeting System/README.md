
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
The robot have a few updates in comparison to lab 2. We have added a wifi shield to allow us to communicate with the robot using Digitrec from lab 3. You will need to use the wifi shield to program the robot to spin initially when we draw a number on Digitrec website. To utilize the wifi shield, some modifications to the wiring of the robot are needed. Follow the tutorial in the folder titled "Communications Tutorial" in order to upgrade your robot. We also have access to the front facing infrared sensor.    

### Tasks
--- 
Your robot must be able to perform the following tasks:

1. Program the wifi shield on the robot to allow it to receive information from the Digitrec website.
2. Spin the robot based on the number drawn on the Digitrec website.
3. Have the robot navigate the maze in shortest possible time.
4. Make sure the robot's intelligence is robust enough that it can handle different maze configurations.

### Design tips
---
1. To help improve navigation time, you can increase the speed of the motors so that the robot can move and turn faster. However, the robot will be less stable and will likely tip over. You will therefore need to improve stability.
2. There are two infrared sensors on the robot. One on the front and one on the bottom; the bottom can help detect the target and the front can be used to sense distance between the sensor and the wall. It is recommended that you utilize the front infrared sensor to allow the robot to see the distance between itself and the wall; think about how the robot will know (or can guess) that it is going the right way. The front infrared sensor can also prevent the robot from getting stuck.
3. The bumpers are an excellent tool to provide information to the robot. Look at the extensions for lab 2 where you implement the bumper to allow the robot to intelligently turn based on which bumper was pressed. 
4. You can use the layout of the maze to your advantage.


### Programming tips
---
As in lab 2, you will be programming in C++ on the Arduino IDE. You will also verify and upload the code using the IDE.
Even though you will use code from lab 2, you will likely find yourself writing more lines code to configure the robot AI. It is therefore very useful to develop good coding practices and tricks in order to organize your code and improve the readability of your code.

### Improving the readability of you code
<details><summary><I>Comments</I></summary>
<p> 
    Since you will be working in a group with other students, comments are a very good way to tell others what your code does as well as help group members debug the code. In C++, comments can be made using ```//```, which comments lines, or ```/*..*/```, which comments a block. 
    Uses for comments:
    - You can comment out code in order to help isolate bugs. 
    - Label variables and functions
    - Insert comments next to lines of code to tell the user what that line does.
    - Put instructions on how to use this code/program.

    You can comment out large blocks of code using ```/*..*/``` and comment specific lines using ```//```. Commented code is ignored by the compiler and will not be uploaded onto the board; thus, it will not take up additional memory.
</p>
</details>


*Header Files*:
Another great way to organize your code is to include header files. The project is divided into different phases and you will likely split up into different groups. Header files is useful for integrating different parts of the project in a single file.

The current project involves multiple parts: wifi, robot control, navigation, and robot peripherals. All these parts require a significant amount of the code.

To create Header files, open any plane text file such as one from a text editor and save the it with the ".h" ending. This marks the file as a C/C++ header file. The default may be a ".txt"; just delete that ending. Save  the ".h" file in the same sketch folder as your main Arduino file. Example shown below.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/figures/ex1.PNG" width="400">
    <font size="2">
        <figcaption> Figure 1: Adding header file to directory <br></br> </a>
    </figcaption>
    </font>
</figure>

When you open your main Arduino ".ino" file. You will see the header file as a tab in your IDE. Shown below.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/figures/ex2.PNG" width="400">
    <font size="2">
        <figcaption> Figure 2: Tabs with header files <br></br> </a>
    </figcaption>
    </font>
</figure>

Now, all you have to do is include the header files in the main file and in any file you plan to use the header file in. This is done using ```#include "(name of header file).h"```. Remember to use the double quotes which tells the compiler that we are adding a file from the same location as the file that included it.

### C++ Tutorial
*Functions*:
Functions are a group of statements that perform a specific task. Function are useful for performing repetitive tasks.
Declare a function like this:
```
return_type function_name( parameter ) {
   body of the function
}
```
Example:
```
void robot_turn(int direction){
	Serial.print(direction);
}
```
In the above example, ```void``` means that the doesn't return anything. ```robot_turn``` is the function name. The parameter is specified the same way as the function with a type and name. The function takes in an integer as a parameter named ```direction``` and prints it out to the Serial monitor. Functions are very useful for abstracting tasks for easiler integration with the rest of the code. You can also make repetitive tasks into functions so that you only need to call the function instead of executing similar lines of code repeatedly.







