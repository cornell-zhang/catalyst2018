Lab 2: Smart Robot
======================

In the previous lab assignment, you explored the field of computer engineering solely from the hardware perspective. In this lab, however, you will start to see how hardware relates to software by programming various behaviors using an Arduino-based robotics platform. In Part 1, you will experiment with the robot's sensors and actuators. Part 1 is intended to teach you about engineering from a software standpoint, so much of the code used to test and experiment with these sensors is provided for you. In Part 2, you will gradually develop a more complicated wandering behavior for your robot. Part 2 will require more critical thinking, as you will be developing much of your own implementation. It will eventually culminate in creating a program that allows your robot to roam an enclosed space and locate a target. The environments your robots will navigate are 4'x3' plywood enclosures, each with a 12"x12" black square target. Your robot should be able to locate the target starting in any location and orientation. 

This lab will require you to devlop mobile robot control application, specifically a closed loop controller.  A closed loop controller operates actuators based on continuously collected and interpreted sensor data. In contrast, an open loop controller utilizes preset information instead of sensors. For example, as closed loop controllers, our robots will use sensors to determine whether they have bumped into an obstacle and will proceed accordingly if they have.  An open loop controller would instead attempt to move in a predefined fashion regardless of whether an obstacle is in the way. Closed loop controllers are a much better option for navigating our environment, as the initial orientation and location of our robot is unknown. 

For each section, you will need to have a teaching assistant observe the desired behavior and initial the appropriate section on the sign-off sheet. **Make sure to turn in your sign-off sheet at the end of the lab session.**

Hardware Description
-------------------------------

Before beginning the lab, make sure to take a look at the components you will need:

- Arduino-based robotics platform
- Wooden testing block (some groups may need to share)
- Workstation with black USB cable

A diagram of the environment your robot will need to navigate is shown below in Figure 1. Once your group gets a mobile robot, take a look at it and try to identify each part of the robot. Diagrams of the top-view and front-view of the robot are shown in Figures 2 and 3 respectively. Figure 4 shows a diagram of the prototyping board. The robot includes two mechanical bump switches at the front to detect obstacles and a grayscale sensor on the bottom to detect the target.  The robot's circuitry includes a stack of three boards mounted on top of the robot.  The lowest board is an Arduino, the main computing board, which you will program. The middle board is a motor shield, which allows the Arduino to control the robot's two motors.  The last board is a maker shield, which connects to the grayscale sensor and the two bump switch sensors. The maker shield also contains LEDs, a button, and a potentiometer.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotEnvironment.png" width="400">
    <font size="2">
        <figcaption> Figure 1: Plywood Environment <br></br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotTop.png" width="400">
    <font size="2">
        <figcaption> Figure 2: Top-View of Mobile Robotic Platform <br></br></a> 
    </figcaption>
    </font>
</figure>

The robot is powered using two different power supplies. Five AA batteries located at the bottom of the robot power the two drive motors.  A separate battery pack will be used to power the board stack.  This will need to be plugged into the Arduino board after the robot is disconnected from the computer in order for the robot to be properly powered. In order to power the drive motors, you will need to flip the motor switch to ON.  If you need to stop your robot from moving, simply switch the drive motor switch to OFF. To test your code, place your robot on the wooden testing block, upload your code, and switch the drive motor to ON.  This will allow you to turn on your robot's drive motors without having it actually move. 


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotFront.png" width="400">
    <font size="2">
        <figcaption> Figure 3: Front-View of Mobile Robotic Platform <br></br></a> 
    </figcaption>
    </font>
</figure>


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PrototypingBoard.png" width="400">
    <font size="2">
    <figcaption> Figure 4: Prototyping Board<br></br> </a> 
    </figcaption>
    </font>
</figure>

Lab Exercises
--------------------------

### Part 1. Robotic Sensors and Acutators
In this part, you will experiment with the various sensors and actuators that you just identified on the robot. This is designed to not only introduce you to the components of the robot, but also accustom you to the software associated with the Arduino that you will be using in the next section.

#### Part 1.A Experiment with LEDs, Switches, and Potentiometer
In this section, you will experiment with code that will either respond to or control the LEDs, the switches, and the potentiometer. 	

In this lab, we will use a C-like programming language that is compatible with our Arduinos. Each program, or "sketch", consists of a sequence of steps that are executed individually. The sketches we will be using consist of different sections.  The first section defines global variables for pin assignments. The second section includes the setup function.  This function is meant to execute only once when the robot is first powered up. After the setup function is the loop function, which is executed over and over again.  Throughout the lab, you will mostly focus on modifying the loop function to change the behavior of your robot. 

We will be using the Arduino Web Editor to write and compile our code. Use a web browser to access the site [create.arduino.cc](https://create.arduino.cc). Sign in using a Google account, and proceed to the web editor. The figure below displays the layout of the web editor. In the lefthand bar, the sketchbook displays the files you have saved to the web editor.  You will be creating several different sketches throughout the course of this lab. When you select the three-dot icon at the top of the page, you can save files you have been editing to the sketchbook. The checkmark icon compiles your current sketch, and the right arrow icon uploads your code to your Arduino board once it has been connected via USB.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/ArduinoWebEditor.png" width="600">
    <font size="2">
    <figcaption> Figure 5: Arduino Web Editor Layout <br></br></a> 
    </figcaption>
    </font>
</figure>

Note that if the Auduino Web Editor keeps reporting errors, please switch to this portable Auduino IDE. 
<a href="https://drive.google.com/drive/folders/18qj4JanxX0zgHVHPIdTbCf_Tizlyk6sP?usp=sharing"> (Link to Folder) </a> You should download this file to the disk and unzip the file which is called "arduino-1.8.5.zip". Then you should enter the corresponding folder and open Arduino GUI by double clicking the executable file called "arduino.exe". Now you should be able to write your code and verify it. Try to explore the menu (File, Edit, Sketch, Tools, and Help) on the top to learn how to use this IDE (Figure 6). 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/Arduino_IDE.PNG" width="600">
    <font size="2">
    <figcaption> Figure 6: Arduino IDE Layout <br></br></a> 
    </figcaption>
    </font>
</figure>

Now, we will program our robot very simply, using the code shown in Figure 7. You should type this code into the Arduino web editor. As you write more programs, you will likely find yourself typing the same code components over and over again. To avoid repetition, you may want to save your file using the menu item: *Save* and then create a new copy for each new part by using the menu item: *Save As…* You can then delete portions of the code that you don’t need for your new project and start working. Once you are finished writing the code shown in Figure 7, upload your code to the Arduino and verify that the LED blinks as it should.  To upload your code to the Arduino, first ensure that the black USB cable is plugged into your computer and the Arduino stack. Check that the battery pack is plugged into the board as well. Compile your code by clicking the checkmark icon.  Note: if errors arise when compiling your code, it is likely that you have one or more syntax errors. In this case, check that your code is exactly the same as the code in Figure 7 and compile it again.  Finally, upload your code by selecting the right arrow icon. After checking that the LED is blinking, you can play around with the delay to vary the blink rate.

Some notes on coding:
- ```//``` before any words means that the entire line is "commented" which doesn't affect the execution of the code in any way. They are good for labeling parts of your code and telling the user how the code works.
- Always remember to put a semicolon ```;``` behind each line of code because that denotes line ending.
- For variables, which are shown in lines 3 to 6, the first word denotes the type of variable.  The second word is the variable name and is set equal to a value. For example, in line 3, ```int pin_led1 = 4``` means that we are declaring a variable of type "integer" named pin_led1 with an integer value of 4.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" width="600">
    <font size="2">
    <figcaption> Figure 7: Blinking LED Code Example <br></br></a> 
    </figcaption>
    </font>
</figure>

We will now extend the code to make one LED light up when the right bumper is pressed and the other light up when the left bumper is pressed. The code for this part is shown in Figure 8 below. Verify that this works as expected after typing the code into the web editor and uploading it to your Arduino.


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" width="600">
    <font size="2">
    <figcaption> Figure 8: Blinking LED and Switch-Controlled LED Code Example<br></br> </a> 
    </figcaption>
    </font>
</figure>


Once this part is working, we can extend the code one step further by getting the potentiometer involved as well. A potentiometer is a variable resistor, and it is located at one end of the prototyping board. Turning the blue knob will change the resistance of the potentiometer. The Arduino can read this resistance as an analog value by using an analog input pin. On our robot, the potentiometer is connected to analog input pin 5. Analog inputs have values between 0 and 1024. You can get the Arduino to read the potentiometer by adding this line to your loop routine:

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PotentiometerReadCode.png" width="600">
</figure>

A small change to the current code can allow the blink rate of the LED to be determined by the potentiometer.  Determine how to implement this new function and modify your code accordingly. After uploading your code, verify that it works properly before showing your results to an instructor.

**Sign-Off Milestone: Once you have one LEDs blink rate controlled by the potentiometer and the other LED controlled by the switch, have a teaching assistant verify that things are working correctly.**

*Critical Thinking Questions*: Explain why pressing the switch quickly sometimes does not turn on the LED, and why the LED stays lit for a short duration after you release the switch. Similarly, explain why adjusting the potentiometer sometimes requires a short duration before impacting the blink rate.


<details><summary><I>HINT 1 (CLICK ME)</I></summary>
<p>
    Don't forget to set up the poteniometer! All peripherals in the Arduino must first be initialized before they can be used. The pin for the potentiometer is already assigned for you at the top titled <code>int pin_potentiometer=A5;</code>. Initialize it like the bumpers and LED's.    
</p>
</details>

<details><summary><I>HINT 2</I></summary>
<p>
   Think about which part of the code sets the flashing rates of the LEDs. It should be a constant value. We want to edit that part of the code so that it changes based on the potentiometer value.
</p>
</details>

<details><summary><I>HINT 3</I></summary>
<p>
    <code>delay</code> takes in an integer value and delays the Arduino by that value in miliseconds. <code>analogRead(pin_potentiometer)</code> allows us to read the potentiometer value as an integer, which can be used to adjust the delay length.   
</p>
</details>

#### Part 1.B Experiment with Grayscale Sensors
In this section, you will experiment with the grayscale sensor on the robot. This is the same sensor you will need to utilize later in the last section to find the location of the target. The grayscale sensor is located on the underside of the robot. Notice that the sensor has both an LED that generates light and a photodetector that senses light. The value the sensor outputs depends on the amount of light that the photodetector senses. This sensor will report values between 0 and 1024, which indicates how much light has been reflected back (lower values indicate that the robot is travelling on a lighter surface, while higher values indicate that the robot is travelling on a darker surface). Enter and upload the code shown in Figure 9 below. We will use the Serial Monitor to observe the value that is output by the grayscale sensor. After uploading the code to the Arduino, you can open up the Serial Monitor by selecting the menu item: *Monitor* in the lefthand bar. Place your robot over the light wood of the testing block and then over the black section of the testing block.  Notice the types of values the grayscale sensor yields in each case and determine a threshold value that separates the two. This value can be a rough estimate of a number that separates grayscale values for light colors and grayscale values for dark colors (you will need to use this value later in the last section). Verify that the readings behave as expected before showing your results to an instructor.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/GrayscaleSensorCode.png" width="600">
    <font size="2">
    <figcaption> Figure 9: Analog Grayscale Sensor and Serial Monitor Example <br></br></a>
    </figcaption>
    </font>
</figure>

**Sign-Off Milestone: Once you have the analog grayscale sensor values being displayed on the serial monitor, have a teaching assistant verify that things are working correctly.** 


#### Part 1.C Experiment with Drive Motors
In this section, you will begin to experiment with the drive motors of the robot. The test program that you will use to experiment with these motors is shown in Figure 9 below. This program will attempt to move the robot in a square with two-foot sides. You will notice that two pins are used to control each drive motor. One pin controls the direction that the motor spins, while the other controls the speed at which that motor spins. When the motor direction output pin is set to LOW, the motor will spin forwards, and when it is set to HIGH, the motor will spin backwards. The motor speed pin can be set to any value between 0 and 255, where higher numbers indicate a faster motor speed. Keep in mind that moderate motor speeds are between 75 and 125, and also that the motor speed is proportional to the voltage generated by the 5 AA batteries(so as they drain, you may have to increase your motor speed in order to get your wheels to turn at the same rate). 

Enter the code shown in Figure 10 below into your Arduino web editor. Once you have done so, place your robot on the testing block to keep it from moving when you are testing. Verify that your robot behaves as expected after uploading the code to your Arduino and, if you would like, try executing this code once more with the robot on the floor so that you can see whether it really does move in a square. If your robot does not move in a square, play around with the rotating delay time until it does. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveRobotSquareCode.png" width="700">
    <font size="2">
        <figcaption> Figure 10: Move Robot in a Square Code Example <br></br></a>
    </figcaption>
    </font>
</figure>

**Sign-Off Milestone: Once you have the robot continuously moving in roughly a square with two-foot sides, have a teaching assistant verify that things are working correctly.**

*Critical Thinking Questions*: Why don’t the same motor speed and delay values always result in every robot moving in a perfect square? If the robot begins moving in a perfect square, does it continue to move in a square? Why or why not? Propose a way to enable the robot to more reliably move in a perfect square. Hint: You probably need to add more sensors to the robot. 

<details><summary><I>HINT 1</I></summary>
<p>
    You can use the potentiometers to quickly adjust the delay time without reprogramming the robot. Implmentation of this feature is very similar to the previous part.    
</p>
</details>

### Part 2. Robotic Behaviors
In this section, you will leverage all that you learned in the previous parts to implement various behaviors for your robot. This will lead up to writing the code that will allow the robot navigate through a maze and locate a certain target. Part A requires you to implement behavior that will make the robot move forward and stop when it hits something. In Part B, you will build off the previous part and allow the robot to display a wandering-to-target behavior. Lastly, you will combine the previous two parts and make the robot spin in a circle when it has reached the target. You will ultimately be building a finite-state machine algorithm (FSM) in your program. An algorithm is a step-by-step procedure that implements an application.  In this case, our application is to control a robot to navigate an environment in search of a target. A finite-state machine algorithm, in particular, utilizes a set of states and state transititions. Our robots will control its motors based on what state it is in and determine when to transitition to a different state based on the sensor data it recieves. 

The figure below illustrates the specific FSM we will be using.  The robot first starts in the FWD state, where it only moves forward.  The robot stays in that state unless one of two events occur: the robot senses an obstacle using its mechanical bump switches or the robot senses the target using its grayscale sensor.  If the robot senses an obstacle, it will move into the REV state, where it will move backward for a fixed amount of time.  It will then transition to the ROT state, where it rotates for a fixed amount of time.  This will allow the robot to first back away from an obstacle and then rotate in a different direction before proceeding. It will then transition back to the FWD state and continue in a different direction.  If the robot senses the target, it will transition to the TGT state, where it will spin in a circle to indicate that it has successfully found the target.  It then will transition to the STOP state.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/FSM_Algorithm.png" width="600">
    <font size="2">
        <figcaption> Figure 11: Finite-State Machine Algorithm <br></br></a>
    </figcaption>
    </font>
</figure>


#### Part 2.A Develop Move-and-Stop Behavior
In this section, you will need to write a program that makes the robot continue to move forward until it hits an obstacle, in which case it will stop. The code shown in Figure 12 below contains a possible starting point for your program.  Be sure to use your wooden testing block when working on this section.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveAndStopTemplateCode.png" width="700">
    <font size="2">
        <figcaption> Figure 12: Template for Move-and-Stop Robot Behavior<br></br> </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT 1</I></summary>
<p>
<code>if(condition){
    }
    else{
    }</code> is a conditional statement that will execute the first part within the curly braces if the first condition evaluates to true. It will execute the second part otherwise. <code> if..else...</code> statements gurantees that one of the two code blocks will be executed and not both.
</p>
</details>

**Sign-Off Milestone: Once you are able to stop your robot by pressing the bump switches, have a teaching assistant verify that things are working correctly.**

*Critical Thinking Questions*: The code above is used to simply program your robot to stop when, and only when, its bump switches are pressed.  Why do you think the robot continues to drive forward as soon as you release the switch? Is it possible for the robot to ever come to a permanent stop? 

#### Part 2.B Develop Wander Behavior
In this section, you will extend the behavior of your robot to include “wandering.” For now, you can ignore the target and just have the robot keep moving forward until it hits an obstacle. When it does, have it reverse and turn slightly. Thus, your robot will keep “wandering” through its environment. Try to build a finite-state machine algorithm that describes the robot’s behavior.  For this part, you will only need to make use of the robot's bump switches and drive motors. Once you think you have it, make sure to check with an instructor. After developing the necessary code and uploading it to the Arduino, verify that your robot behaves as expected.

**Sign-Off Milestone: Once you have the robot successfully wandering the environment, have a teaching assistant verify that things are working correctly.**

*Troubleshooting:* If your robot repeatedly stops before the mechanical bump switches are pressed, it could be due to noise created by the drive motors that causes the robot to behave as if the switches have been pressed. A simple software fix to this problem is to implement code that checks the mechanical bump switches twice with a small delay in between checks. If the bump switch is closed during both checks it is very likely that the robot has actually bumped into an obstacle. 


<details><summary><I>HINT 1</I></summary>
<p>
    Think about the possible states the robot will be in: moving and hit obstacle. We need to continuously check which state the robot is in using conditionals. What conditions must be met for a robot to have hit an obstacle?
</p>
</details>


<details><summary><I>HINT 2</I></summary>
<p>
    It's a good idea to first write the process in English before writing the code. This is called pseudocode. Initialize the states by assigning arbitrary numbers to them. First, check the current state of the robot, then use the current state of the robot to decide which action to perform.  
</p>
</details>

<details><summary><I>HINT 3</I></summary>
<p>
Design algorithm:
    <code>if(hit wall), state = hit wall. else, state = moving</code>
    <code>if(state==hit wall), turn some amount. else if (state==moving), turn wheels to move forward</code>
</p>
</details>

#### Part 2.C Develop Wander-to-Target Behavior

Lastly, you will extend the code from the previous section to include making the robot spin in a circle and stop once it has found the target. If you need to, you can go back and review the code shown in Figure 8, which allowed you to experiment with the grayscale sensor. You may find that the finite-state machine algorithm you made in the previous part will help you with developing your code. Feel free to plan your code and discuss with the teaching assistants before actually beginning to implement it. 

As a hint, we recommend adding code to your loop that reads the analog grayscale sensor. You will need to create an additional conditional if statement that depends on the threshold value of the analog grayscale sensor that you found in Section 2.B. Finally, to stop the robot you might consider just using a delay statement with a very long delay value (e.g. 10 seconds). After you have finished, upload your code to the Arduino and verify that the robot behaves as expected on the provided maze. 

If you would like to optimize the wandering behavior of your robot through the maze, try modifying your code so that the direction the robot turns depends on which mechanical bump switch was pressed. This would allow the robot to turn away from the obstacles it bumps into, thereby allowing it to navigate the maze more quickly.  In other words, program the robot to turn right if the left bump switch is closed and left if the right bump switch is closed. This will require you to find the relevant conditional from the template and instead create two separate conditionals: one for the right bump switch and one for the left. 

**Sign-Off Milestone: Once you have the robot successfully wandering the environment and finding the target, have a teaching assistant verify that things are working correctly.**

<details><summary><I>HINT 1</I></summary>
<p>
The possible states are: looking, found, hit obstacle. You can add more if needed. Remember to initialize the state for when the robot turns on!
</p>
</details>

<details><summary><I>HINT 2</I></summary>
<p>
When trying to find your target, it is a good idea to specify a range of values that are acceptable since the value detected by the grayscale sensor may not be exactly the same every time. Also, the black color of the target may not be exactly the same throughout.  
</p>
</details>

<details><summary><I>HINT 3</I></summary>
<p>
    A good way for specifying a range for the greyscale sensor:
    <code>|sensor_value-target_value|<=threshhold</code>
</p>
</details>

### Optional Extensions: 
---
Parts 1–3 are the required portions of the lab. If you complete these parts quickly, you are free to try one or more of the following extensions which are roughly arranged in order of difficulty. You can also make up your extension. These extensions are purely optional; do not feel like you must attempt them.
- LED State Indicators – Modify your program so that LED1 turns on when the robot is in the REV state, LED2 turns on when the robot is in the ROT state, and both LEDs turn on when the robot finds the target.
- Potentiometer Controlled Speed – Modify your program so that the potentiometer on the prototyping board controls the motor speed.
- Randomized Wandering – Modify your program so that the robot randomly determines which direction to rotate and for how long to rotate. How does this impact the robot’s ability to explore the space and find the target?
- Predefined Pattern – Modify your program so that if the button on the top of the prototyping board is pressed, the robot will move in a predefined pattern (e.g., move in a square) before continuing to wander the space. Your robot should abort the pattern and return to the wandering behavior if it encounters an obstacle while trying to complete the predefined pattern. Can you modify the finite-state machine diagram to appropriately reflect this new behavior?

#### Acknowledgements 
This lab handout is derived from the 2014 CURIE Academy "Computer Engineering -- Software Perspective" lab designed by Professor Christopher Batten.

