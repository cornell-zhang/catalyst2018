
# Rapid Targeting System 
---

### Goal 
---
Use the robot to navigate a maze using various sensors. We will have a competition between groups to see which robot can navigate the maze the fastest. You are allow to use all sensors installed on the robot and read their values to help you accomplish this task. If you have forgotten which sensors are on the robot, you may look on the handout for Lab 2, for a diagram of the sensors on the robot. There are also some sensors that you haven't already used in Lab 3, which you can experiement with, so that you know which sensors you will be using to complete this project.

### Obstacle Course
---
The maze you will be navigating in this project, is the very same one that you had used in Lab 2. It's square in shape, covered on all sides with wooden walls and has a single wooden wall that extends halfway through the middle of the maze. The floor of the maze is entirely wood except for a black square that signifies the target location. The robot will start at a randomly chosen position on the opposite side of the wall from the target and each time, before beginning, it will spin some number of degrees according to the number you write on your Digitrec system. We will provide more detail about how you should have your robot spin, later on in this handout.

We may add more obstacles to the course in order to test the robustness of your robot intelligence. We can also change the starting location of the robot.

### Robot Specification
---
The robot has a few updates in comparison to Lab 2. We have added a wifi chip to allow us to communicate with the robot using your Digitrec system from Lab 3. You will need to use the wifi chip to first receive a handwritten digit from your Digitrec system and then program the robot to spin initially, depending on this number. To utilize the wifi chip, some modifications to the wiring of the robot are needed. Follow the tutorial in the folder titled "Communications Tutorial" in order to upgrade your robot. We also have access to the front facing infrared sensor. You should split your group into two subgroups. One subgroup will be responsible for setting up the communication channel(a.k.a the wifi chip) and testing to see whether the Digitrec system works properly, while the other subgroup will be responsible for testing out the sensors and having the robot navigate to the target in the fastest way possible. After the two subgroups have finished their respective parts, you should integrate the two parts together into one, single piece of Arduino code that you can upload to the robot and have it meet the specifications we have just listed. You will find more detail about the expectations, further down in the handout.

### Tasks
--- 
Your robot must be able to perform the following tasks:

1. Program the CC3000 WiFi board on the robot to allow it to receive information from the Digitrec website.
2. Spin the robot based on the number drawn on the Digitrec website. The degree to spin is scaled to 360 degrees. For example: 0 would be 0 degrees, 1 would be 36 degrees approximately and 9 would be 324 degrees approximately. 
3. Have the robot navigate the maze in shortest possible time.
4. Make sure the robot's intelligence is robust enough that it can handle different maze configurations.
5. When the robot reaches the target, it should spin 360 degrees and stop moving.


### Design tips
---
1. To help improve navigation time, you can increase the speed of the motors so that the robot can move and turn faster. However, the robot will be less stable and will likely tip over. You will therefore need to adjust the speed enough, so that you have a combination of speed and stability. The only way to do this, is to test your design multiple times and adjust the speed accordingly.
2. There are two infrared sensors on the robot. One on the front and one on the bottom; the bottom can help detect the target and the front can be used to sense distance between the sensor and the wall. It is recommended that you utilize the front infrared sensor to allow the robot to see the distance between itself and the wall; think about how the robot will know (or can guess) that it is going the right way. The front infrared sensor can also prevent the robot from getting stuck. The front facing infrared sensor will be useful for getting the robot out corners where bumpers can't detect.  
3. The bumpers are an excellent tool to provide information to the robot. You may refer to the Lab 2 handout to see how you can use the bumper information to get your robot to navigate faster through the maze.

### Programming tips
---
As in lab 2, you will be programming in C++ on the Arduino IDE. You will also verify and upload the code using the IDE.
Even though you will use code from lab 2, you will likely find yourself writing more lines code to configure the robot AI. It is therefore very useful to develop good coding practices and tricks in order to organize your code and improve the readability of your code.

### Improving the readability of you code
<details><summary><b>Comments</b></summary>
<p> 
    Since you will be working in a group with other students, comments are a very good way to tell others what your code does as well as help group members debug the code. In C++, comments can be made using <code>//</code>, which comments lines, or <code>/*..*/</code>, which comments a block. 
</p>
<p>
    Uses for comments:
    <ul>
    <li>You can comment out code in order to help isolate bugs. </li>
    <li> Label variables and functions.</li>
    <li> Insert comments next to lines of code to tell the user what that line does.</li>
    <li> Put instructions on how to use this code/program.</li>
    </ul>
</p>
<p>
    You can comment out large blocks of code using <code>/*..*/</code> and comment specific lines using <code>//</code>. Commented code is ignored by the compiler and will not be uploaded onto the board; thus, it will not take up additional memory.
</p>
</details>

<details><summary><b>Header Files</b></summary>
<p> 
Another great way to organize your code is to include header files. The project is divided into different phases and you will likely split up into different groups. Header files is useful for integrating different parts of the project in a single file.
</p>
 <p> 
The current project involves multiple parts: wifi, robot control, navigation, and robot peripherals. All these parts require a significant amount of the code.
</p> <p> 
To create Header files, open any plane text file such as one from a text editor and save the it with the ".h" ending. This marks the file as a C/C++ header file. The default may be a ".txt"; just delete that ending. Save  the ".h" file in the same sketch folder as your main Arduino file. Example shown below.
</p> 
<font size="2">
        <p>Figure 1: Adding header file to directory</p>
    </font>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/figures/ex1.PNG" width="400">
</figure>
<p> 
When you open your main Arduino ".ino" file. You will see the header file as a tab in your IDE. Shown below.
</p> 
<font size="2">
        <p> Figure 2: Tabs with header files</p>
    </font>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/figures/ex2.PNG" width="400">
</figure>
<p> 
Now, all you have to do is include the header files in the main file and in any file you plan to use the header file in. This is done using ```#include "(name of header file).h"```. Remember to use the double quotes which tells the compiler that we are adding a file from the same location as the file that included it.
</p> 
</details>


<details><summary><b>Finite State Machines</b></summary>
<p>Your robot will need to perform a wide variety of tasks and each task requires a specific set of actions. Finite state machines are very useful and quick way to delegate tasks to your robot depending on the current situation. </p>
<p>Figure 3 below illustrates an example of an FSM. Each circle shows the state of the robot. </p>
<font size="2">
        <p> Figure 3: FSM Algorithm</p>
    </font>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/figures/FSM_Algorithm.png" width="500">
</figure>
<p>To implement a FSM in software, we use case statements where we check for the current state of the robot as well as the next state of the robot.</p>
<pre><code>
switch(state)
  {
    case looking: 
    {
        forward();
        break;
    }
    case hit_wall: 
    {
        reverse(); 
        break;
    }
    case found_target: 
    {
        rotate(); 
        break;
    }
</code></pre>
</details>


### C++ Tutorial
<details><summary><b>Functions</b></summary>
<p>Functions are a group of statements that perform a specific task. Function are useful for performing repetitive tasks.</p>
<p>Declare a function like this:
<pre><code>
return_type function_name( parameter ) {
    body of the function
}
</code></pre>
Example:
<pre><code>
void robot_turn(int direction){
    Serial.print(direction);
}
</pre></code></p>
<p>
In the above example, <code>void</code> means that the doesn't return anything. <code>robot_turn</code> is the function name. The parameter is specified the same way as the function with a type and name. The function takes in an integer as a parameter named <code>direction</code> and prints it out to the Serial monitor. Functions are very useful for abstracting tasks for easiler integration with the rest of the code. You can also make repetitive tasks into functions so that you only need to call the function instead of executing similar lines of code repeatedly.
</p>
</details>





