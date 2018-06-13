Lab 2: Smart Robot
======================

In the previous lab assignment, you explored the field of computer engineering solely from the hardware perspective. In this lab, however, you will start to see how the hardware relates to software by programming various behaviors on an Arduino-based robotics platform. In the first part of this lab, you will experiment with sensors and actuators on the robot. Much of the code to test and experiment with these sensors is provided for you, so that you can ease your way into learning about both the software and how that relates to the hardware. In the second section, you will develop a more complicated wandering behavior for your robot, which eventually culminates in programming your robot to reach a target. For each section, you will need to have a teaching assistant observe the desired behavior and initial the appropriate section on the sign-off sheet. **Make sure to turn in your sign-off sheet at the end of the lab session.**

Hardware Description
--------------------------------

Before beginning the lab, make sure to take a look at the components that you will need:

- Arduino-based robotics platform
- Wooden testing block (some groups may need to share)
- Workstation with black USB cable
- Arduino cheat sheet

Take a look at the mobile robotic platform and try to identify each of the parts of the robot when your group gets one. Diagrams of the top-view and front-view of the robot are shown in Figures 1 and 2, respectively, while Figure 3 shows a diagram of the prototyping board.

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
In this part, you will experiment with the various sensors and actuators that you just identified on the robot. This will not only gradually introduce you to the sensors/actuators on the robot, but also get you much more comfortable with the software associated with the Arduino that you will be using to program different behaviors for your robot when doing the tasks in the next section.

#### Part1.A Experiment with LEDs, Switches, and Potentiometer
In this section, you will experiment with code that will either respond to or control the LEDs, switches, and potentiometer. 	

Now, we will program our robot very simply, using the code shown in Figure 4. You should type up this code into the Arduino IDE. As make more and more programs having to do with the robot, you will likely find yourself typing the same things over and over again. To avoid doing this many times, you may want to save your file using the menu item: File → Save and then create a new copy for this part by using the menu item: *File → Save As* … You can then delete portions of the code that you don’t need for your new project and start working. Once you are finished writing the code shown in Figure 4, upload your code to the Arduino and verify that the LED blinks as it should.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" target="_blank">Link to image of blinking LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 4: Blinking LED Code Example </a> 
    </figcaption>
    </font>
</figure>

Once this is working properly, let’s try to extend the code we’ve just written such that we make one LED light up when the right bumper is pressed and the other light up when the other LED is pressed. The code for this part is shown in Figure 5 below. Verify that this works as expected after finishing and uploading the code to your Arduino.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" target="_blank">Link to image of blinking LED and switch-controlled LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 5: Blinking LED and Switch-Controlled LED Code Example </a> 
    </figcaption>
    </font>
</figure>

Once this part is working, we can extend the code one step further, but getting the potentiometer involved as well. A potentiometer is a variable resistor, and it is located on one end of the prototyping board. Turning the blue knob will change the resistance of the potentiometer. The Arduino can read this resistance as an analog value by using an analog input pin. On our robot, the potentiometer is connected to analog input pin 5, and you will observe that analog inputs have values between 0 and 1023 when you add this extra functionality to your code. You can get the Arduino to read the potentiometer by adding this line to your loop routine:

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PotentiometerReadCode.png" width="400">
</figure>

After adding this statement to your code, verify that it works properly before showing your results to an instructor.

*Sign-Off Milestone*: Once you have one LED’s blink rate controlled by the potentiometer and the other LED controlled by the switch, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: Explain why pressing the switch quickly sometimes does not turn on the LED, and why the LED stays lit for a short duration after you release the switch. Similarly, explain why adjusting the potentiometer sometimes requires a short duration before impacting the blink rate.

#### Part1.B Experiment with Grayscale Sensors
In this section, you will experiment with the grayscale sensor on the robot, before you have to use it to find the location of the target in the last section. The grayscale sensor is located on the underside of the robot. Notice that the sensor has both a LED that generates light and a photodetector that senses light. Depending on the amount of light that the photodetector senses, it will output a different sort of value. This sensor will also report values between 0 and 1023, which indicates how much light has been reflected back(so lower values indicate that the robot is travelling on a lighter surface, while higher values will indicate that the robot is travelling on a darker surface). Enter and upload the code shown in Figure 6 below. We will use the Serial Monitor to observe the value that is output by the grayscale sensor. After uploading the code to the Arduino, you can open up the serial monitor by selecting the menu item: Tools → Serial Monitor. Verify that the readings behave as expected, before showing your results to an instructor.

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

#### Part1.C Experiment with Drive Motors
In this section, you will begin to experiment with the drive motors of the robot. The test program that you will use to experiment with these motors is shown in Figure 7 below. This program will attempt to move the robot in a square pattern, with sides being two feet long. You will notice that two pins are used to control leach drive motor. One pin controls the direction that the motor spins, while the other controls the speed at which that motor spins. When the motor direction output pin is set to LOW, the motor will spin forwards, and when it is set of HIGH, the motor will spin backwards. The motor speed pin can be set to any value between 0 and 255, where higher numbers indicate a faster motor speed. Keep in mind that moderate motor speeds are between 75 and 125, and also that the motor speed is proportional to the voltage generated by the 5 AA batteries(so as they drain, you may have to increase you motor speed in order to get your wheels to turn at the same rate). 

Enter the code shown in Figure 7 below, into your Arduino IDE. Once you have done so, place your robot onto the testing block to keep it from moving when you are testing. Verify that your robot behaves as expected after uploading the code to your Arduino, and if you would like, try executing this code once more, with the robot on the floor, so that you can see whether it really does move in a square.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveRobotSquareCode.png" target="_blank">Link to image of move robot in a square code</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveRobotSquareCode.png" width="400">
    <font size="2">
        <figcaption> Figure 7: Move Robot in a Square Code Example </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have the robot continuously moving in roughly a square with two-foot sides, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: Why don’t the same motor speed and delay values always result in every robot moving in a perfect square? If the robot begins moving in a perfect square, does it continue to move in a square? Why or why not? Propose a way to enable the robot to more reliably move in a perfect square; Hint: You probably need to add more sensors to the robot. Explain the difference between an open loop controller and a closed loop controller.

(Need to add Debug Hints)

### Part 2. Robotic Behaviors
In this section, you will leverage all that you learned in the previous parts in order to implement various behaviors for your robot. This will all lead up to you writing the code that will allow the robot navigate through a maze and locate a certain target. This first part will have you implement behavior that will make the robot move forwards and stop when it hits something. The second part will have you build off the first part and allow the robot to display a wandering-to-target behavior. Lastly, you will combine the previous two parts and make the robot spin in a circle when it has reached the target.

It is recommended that you start with a fresh version of the code template provided for you. If you haven’t done so already, you can access the template by choosing the following menu item: *File → Sketchbook → catalyst_lab2_template*. Delete old code in the loop routine so that you can start writing on a clean slate.


#### Part2.A Develop Move-and-Stop Behavior
In this section, you will have to write a program that makes the robot keep moving forwards until it hits an obstacle— in which case it will stop. The code shown in Figure 8 below, contains a possible starting point for your program.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveAndStopTemplateCode.png" target="_blank">Link to image of template for move and stop behavior code</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/MoveAndStopTemplateCode.png" width="400">
    <font size="2">
        <figcaption> Figure 8: Template for Move-and-Stop Robot Behavior </a>
    </figcaption>
    </font>
</figure>

#### Part2.B Develop Wander Behavior
In this section, you will extend the behavior of your robot to include “wandering”. For now, you can ignore the target and just have the robot keep moving forward until it hits an obstacle. When it does, have it reverse and turn slightly. Thus, your robot will keep “wandering” through its environment. Try to build a finite-state machine algorithm that describes the robot’s behavior. Once you think you have it, make sure to check with an instructor. After developing the necessary code as well, and uploading it to the Arduino, verify that your robot behaves as expected.

*Sign-Off Milestone*: Once you have the robot successfully wandering the environment, have a teaching assistant verify that things are working correctly

#### Part2.C Develop Wander-to-Target Behavior

Lastly, you will extend the code from the previous section to include making the robot spin in a circle and stop once it has found the target. If you need to, you can go back and review the code shown in Figure 6, which allowed you to experiment with the grayscale sensor. You may find that the finite-state machine algorithm that you made in the previous part will help you with developing your code. Feel free to plan out your code on paper and discussing with the teaching assistants, before actually beginning to implement it. 

As a hint, we recommend adding some code after you check the bump switches to read the analog grayscale sensor. If the value from the analog grayscale sensor is greater than the threshold you found in Section 2.B set a variable to one otherwise set this variable to zero. Then you can use this variable to create an additional if/then conditional control statement similar to what we have used to handle obstacles. Finally, to stop the robot you might consider just using a delay statement with a very long delay value (e.g., 10 seconds). After you have finished, upload your code to the Arduino and verify that the robot behaves as expected on the provided maze.

*Sign-Off Milestone*: Once you have the robot successfully wandering the environment and finding the target, have a teaching assistant verify that things are working correctly.
