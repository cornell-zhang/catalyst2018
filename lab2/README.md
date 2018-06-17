Lab 2: Smart Robot
======================

In the previous lab assignment, you explored the field of computer engineering solely from the hardware perspective. In this lab, however, you will start to see how hardware relates to software by programming various behaviors using an Arduino-based robotics platform. In Part 1, you will experiment with the robot's sensors and actuators. Part 1 is intended to teach you about engineering from a software standpoint, so much of the code used to test and experiment with these sensors is provided for you. In Part 2, you will gradually develop a more complicated wandering behavior for your robot. It will eventually culminate in creating a program that allows your robot to roam an enclosed space and locate a target. Part 2 will require more critical thinking, as you will be developing much of your own implementation. For each section, you will need to have a teaching assistant observe the desired behavior and initial the appropriate section on the sign-off sheet. **Make sure to turn in your sign-off sheet at the end of the lab session.**

Hardware Description
--------------------------------

Before beginning the lab, make sure to take a look at the components that you will need:

- Arduino-based robotics platform
- Wooden testing block (some groups may need to share)
- Workstation with black USB cable
- Arduino cheat sheet

Take a look at the mobile robotic platform and try to identify each part of the robot when your group gets one. Diagrams of the top-view and front-view of the robot are shown in Figures 1 and 2 respectively. Figure 3 shows a diagram of the prototyping board.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotTop.png" target="_blank">Link to image of top view of robot</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotTop.png" width="300">
    <font size="2">
    <figcaption> Figure 1: Top-View of Mobile Robotic Platform </a> 
    </figcaption>
    </font>
</figure>

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotFront.png" target="_blank">Link to image of front view of robot</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/RobotFront.png" width="300">
    <font size="2">
    <figcaption> Figure 2: Front-View of Mobile Robotic Platform </a> 
    </figcaption>
    </font>
</figure>

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PrototypingBoard.png" target="_blank">Link to image of prototyping board</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PrototypingBoard.png" width="300">
    <font size="2">
    <figcaption> Figure 3: Prototyping Board </a> 
    </figcaption>
    </font>
</figure>

Lab Exercises
--------------------------

### Part 1. Robotic Sensors and Acutators
In this part, you will experiment with the various sensors and actuators that you just identified on the robot. This is designed to not only introduce you to the components of the robot, but also accustom you to the software associated with the Arduino that you will be using in the next section.

#### Part 1.A Experiment with LEDs, Switches, and Potentiometer
In this section, you will experiment with code that will either respond to or control the LEDs, the switches, and the potentiometer. 	

Now, we will program our robot very simply, using the code shown in Figure 4. You should type this code into the Arduino IDE. As you write more programs, you will likely find yourself typing the same code components over and over again. To avoid doing this many times, you may want to save your file using the menu item: File → Save and then create a new copy for each new part by using the menu item: *File → Save As* … You can then delete portions of the code that you don’t need for your new project and start working. Once you are finished writing the code shown in Figure 4, upload your code to the Arduino and verify that the LED blinks as it should.  To upload your code to the Arduino, first ensure that the black USB cable is plugged into your computer and the Arduino stack. Verify that your Arduino IDE is connected to the right serial port by clicking Tools → Port. Check that the 9V battery is plugged into the board as well. Compile your code by clicking the checkmark icon.  Note: if errors arise when compiling your code, it is likely that you have one or more syntax errors. In this case, check that your code is exactly the same as the code in Figure 4 and compile it again.  Finally upload your code by selecting the right arrow icon. After checking that the LED is blinking, you can play around with the delay to vary the blink rate.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" target="_blank">Link to image of blinking LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 4: Blinking LED Code Example </a> 
    </figcaption>
    </font>
</figure>

We will now extend the code to make one LED light up when the right bumper is pressed and the other light up when the left bumper is pressed. The code for this part is shown in Figure 5 below. Verify that this works as expected after typing the code into the IDE and uploading it to your Arduino.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" target="_blank">Link to image of blinking LED and switch-controlled LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 5: Blinking LED and Switch-Controlled LED Code Example </a> 
    </figcaption>
    </font>
</figure>

Once this part is working, we can extend the code one step further, by getting the potentiometer involved as well. A potentiometer is a variable resistor, and it is located on one end of the prototyping board. Turning the blue knob will change the resistance of the potentiometer. The Arduino can read this resistance as an analog value by using an analog input pin. On our robot, the potentiometer is connected to analog input pin 5. Analog inputs have values between 0 and 1023. You can get the Arduino to read the potentiometer by adding this line to your loop routine:

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PotentiometerReadCode.png" width="400">
</figure>

A small change to the current code can allow the blink rate of the LED to be determined by the potentiometer.  Determine how to implement this new function and modify your code accordingly. After uploading your code, verify that it works properly before showing your results to an instructor.

*Sign-Off Milestone*: Once you have one LED’s blink rate controlled by the potentiometer and the other LED controlled by the switch, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: Explain why pressing the switch quickly sometimes does not turn on the LED, and why the LED stays lit for a short duration after you release the switch. Similarly, explain why adjusting the potentiometer sometimes requires a short duration before impacting the blink rate.

#### Part 1.B Experiment with Grayscale Sensors
In this section, you will experiment with the grayscale sensor on the robot. This is the same sensor you will need to utilize later in the last section to find the location of the target. The grayscale sensor is located on the underside of the robot. Notice that the sensor has both an LED that generates light and a photodetector that senses light. The value the sensor outputs depends on the amount of light that the photodetector senses. This sensor will report values between 0 and 1024, which indicates how much light has been reflected back (lower values indicate that the robot is travelling on a lighter surface, while higher values indicate that the robot is travelling on a darker surface). Enter and upload the code shown in Figure 6 below. We will use the Serial Monitor to observe the value that is output by the grayscale sensor. After uploading the code to the Arduino, you can open up the serial monitor by selecting the menu item: *Tools → Serial* Monitor. Place your robot over the light wood of the testing block and then over the black section of the testing block.  Notice the types of values the grayscale sensor yields in each case and determine a threshold value that separates the two. This value can be a rough estimate of a number that separates grayscale values for light colors and grayscale values for dark colors (you will need to use this value later in the last section). Verify that the readings behave as expected before showing your results to an instructor.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/GrayscaleSensorCode.png" target="_blank">Link to image of grayscale sensor and serial monitor example code</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/GrayscaleSensorCode.png" width="400">
    <font size="2">
    <figcaption> Figure 6: Analog Grayscale Sensor and Serial Monitor Example </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have the analog grayscale sensor values being displayed on the serial monitor, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: What happens when the analog grayscale sensor is positioned precisely at the edge of the target? How do your readings compare to the readings collected by other groups around you? Why do you think all robots do not report the same analog grayscale sensor values when positioned over similar materials? What do you think would happen if the target was made out of a very glossy black material?

#### Part 1.C Experiment with Drive Motors
In this section, you will begin to experiment with the drive motors of the robot. The test program that you will use to experiment with these motors is shown in Figure 7 below. This program will attempt to move the robot in a square pattern, with sides being two feet long. You will notice that two pins are used to control each drive motor. One pin controls the direction that the motor spins, while the other controls the speed at which that motor spins. When the motor direction output pin is set to LOW, the motor will spin forwards, and when it is set to HIGH, the motor will spin backwards. The motor speed pin can be set to any value between 0 and 255, where higher numbers indicate a faster motor speed. Keep in mind that moderate motor speeds are between 75 and 125, and also that the motor speed is proportional to the voltage generated by the 5 AA batteries(so as they drain, you may have to increase you motor speed in order to get your wheels to turn at the same rate). 

Enter the code shown in Figure 7 below, into your Arduino IDE. Once you have done so, place your robot on the testing block to keep it from moving when you are testing. Verify that your robot behaves as expected after uploading the code to your Arduino, and if you would like, try executing this code once more, with the robot on the floor, so that you can see whether it really does move in a square. If your robot does not move in a square, play around with the rotating delay time until it does. 

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveRobotSquareCode.png" target="_blank">Link to image of move robot in a square code</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveRobotSquareCode.png" width="400">
    <font size="2">
        <figcaption> Figure 7: Move Robot in a Square Code Example </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have the robot continuously moving in roughly a square with two-foot sides, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: Why don’t the same motor speed and delay values always result in every robot moving in a perfect square? If the robot begins moving in a perfect square, does it continue to move in a square? Why or why not? Propose a way to enable the robot to more reliably move in a perfect square; Hint: You probably need to add more sensors to the robot. 


### Part 2. Robotic Behaviors
In this section, you will leverage all that you learned in the previous parts to implement various behaviors for your robot. This will lead up to writing the code that will allow the robot navigate through a maze and locate a certain target. Part A requires you to implement behavior that will make the robot move forwards and stop when it hits something. In Part B, you will build off the previous part and allow the robot to display a wandering-to-target behavior. Lastly, you will combine the previous two parts and make the robot spin in a circle when it has reached the target.

#### Part 2.A Develop Move-and-Stop Behavior
In this section, you will have to write a program that makes the robot keep moving forwards until it hits an obstacle— in which case it will stop. The code shown in Figure 8 below, contains a possible starting point for your program.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveAndStopTemplateCode.png" target="_blank">Link to image of template for move and stop behavior code</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveAndStopTemplateCode.png" width="400">
    <font size="2">
        <figcaption> Figure 8: Template for Move-and-Stop Robot Behavior </a>
    </figcaption>
    </font>
</figure>

#### Part 2.B Develop Wander Behavior
In this section, you will extend the behavior of your robot to include “wandering”. For now, you can ignore the target and just have the robot keep moving forward until it hits an obstacle. When it does, have it reverse and turn slightly. Thus, your robot will keep “wandering” through its environment. Try to build a finite-state machine algorithm that describes the robot’s behavior.  For this part, you will only need to make use of the robot's bump switches and drive motors. Once you think you have it, make sure to check with an instructor. After developing the necessary code and uploading it to the Arduino, verify that your robot behaves as expected.

*Sign-Off Milestone*: Once you have the robot successfully wandering the environment, have a teaching assistant verify that things are working correctly

*Troubleshooting:* If your robot repeatedly stops before the mechanical bump switches are pressed, it could be due to noise created by the drive motors that causes the robot to behave as if the switches have been pressed.  A simple software fix to this problem is to implement code that checks the mechanical bump switches twice with a small delay in between checks.  If the bump switch is closed during both checks it is very likely that the robot has actually bumped into an obstacle. 

#### Part 2.C Develop Wander-to-Target Behavior

Lastly, you will extend the code from the previous section to include making the robot spin in a circle and stop once it has found the target. If you need to, you can go back and review the code shown in Figure 6, which allowed you to experiment with the grayscale sensor. You may find that the finite-state machine algorithm you made in the previous part will help you with developing your code. Feel free to plan your code and discuss with the teaching assistants before actually beginning to implement it. 

As a hint, we recommend adding code to your loop that reads the analog grayscale sensor. You will need to create an additional conditional if statement that depends on the threshold value of the analog grayscale sensor that you found in Section 2.B. Finally, to stop the robot you might consider just using a delay statement with a very long delay value (e.g., 10 seconds). After you have finished, upload your code to the Arduino and verify that the robot behaves as expected on the provided maze. 

If you would like to optimize the wandering behavior of your robot through the maze, try modifying your code so that the direction the robot turns depends on which mechanical bump switch was pressed. This would allow the robot to turn away from the obstacles it bumps into, thereby allowing it to navigate the maze more quiickly.  In other words, program the robot to turn right if the left bump switch is closed and left if the right bump switch is closed. This will require you to find the relevant conditional from the template and instead create two separate conditionals: one for the right bump switch and one for the left. 

*Sign-Off Milestone*: Once you have the robot successfully wandering the environment and finding the target, have a teaching assistant verify that things are working correctly.
