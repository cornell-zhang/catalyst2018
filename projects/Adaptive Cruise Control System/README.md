Project 2: Adaptive Cruise Control System
======================
In this project, you will equip your robot with an adaptive cruise control system and install a remote control mechanism that will allow you to control the speed of your robot using the digit recognition system implemented in Lab 3. An adaptive cruise control system automatically regulates the distance between a car and other cars and obstacles. This system adapts the speed of the car based on its distance to other cars and objects, and serves as the the basis for making "smart" self-driving cars. 

In this lab, you will implement a version of an adaptive cruise control system, albeit one that's much simpler than those used in self-driving systems. While there are many possible features that you can implement, as the core of this project, you will use the infrared sensor attached to detect the distance between your robot and any obstacle that may be in front of it. Based on the distance to the nearest obstacle in front of it, you should make your robot change speeds accordingly. To implement remote control, we will provide you with a code template for connecting your robot to the WiFi after minimal amount of rewiring. This will allow you to control your robot by drawing digits on the canvas from Lab 3.

This project can be divided into independent tasks. Each group should further divide into subgroups to work on different tasks in parallel. At the end, different subgroups will come together to assemble the final system. Each group will get multiple robots to experiment with their design so that each subgroup has its own robot to work with.

### Task 1: Setting up the wireless connection
For this final project, your robots will need to have Internet connection capabilities.  For this reason, we will be using a different type of board in place of the Arduino Uno you previously used. We will be using a Seeeduino board, which has an integrated Wifi chip. Once your group has received a Seeeduino, please carefully remove the Arduino Uno from the bottom of your robot's circuit board stack, and plug in the Seeeduino instead. The Seeeduino should be able to attach to the board stack in the same manner as the Arduino Uno. Please take extra precaution when aligning the pins so that pins do not get bent and damaged. 

When using the Arduino web editor to program your robot, you will need to change the board type. Select the drop-down bar at the top that currently reads "Arduino Uno" then click "Select Other Board & Port."  Choose the "Arduino Yun" option. To allow each group to simultaneously use the digit recognition web server to control their robot, each group must connect to a different port. Each Seeeduino board has a unique MAC address and has been bound to a specific port in our router. When using our code template, be sure to locate the `#define PORT #` line and change the number to your group number. When signing in to the digit rec web server, you should also be sure to sign into the account corresponding to your correct group number. 

Specific instructions on the WiFi connection and port numbers are provided as part of the [Seeeduino communication tutorial](../Communication%20Tutorial/Seeeduino). Please carefully read this tutorial before completing the task. You can find the port that you will have to change to, along with the appropriate group number, by referring to the table that in the communication tutorial. A [code template](Project2Template.ino) is also provided for you to receive the digit. Please pay close attention to the `receive_value` function and take advantage of it accordingly.

**Milestone 1.1: Your robot should be able to receive any digit sent from our digit recognition web app. You should verify the received digit with the serial monitor.**

**Milestone 1.2: Your robot should be able adjust the speed of the motors based on the value of the digit sent from the web app. For example, your motors should rotate faster for a larger digit.**

### Task 2: Developing the cruise control system 
For this task, you will develop and test the core components of your cruise control system. Most importanly, you should determine a function that will relate your desired speed with the distance values received from the infrared sensor. Your speed value should have an inverse (opposite) relationship with distance, as your robot should drive slowly when it is near objects and drive at a faster speed when it is far away from objects.  Speeds should range from 0 to approximately 125 in order to ensure that the robot does not drive at an unreasonably fast speed.  You might find it helpful to first print out distance values from the infrared sensor over the serial monitor in order to determine the range of distance values.  If you forget how to print out values over the serial monitor, feel free to reference your code from Lab 2 (the grayscale sensor code might be helpful). As a hint, be sure that your loop function continuously reads infrared sensor values, uses your distance-to-speed function to determine a speed based on this distance value, and sets the speed-controlling pins of the Arduino to these values.  Test your cruise control system by uploading it to the robot and seeing if you can observe a noticeable difference in speed when you move your hand closer to the robot.

**Milestone 2.1: Your robot should be able to detect the distance to any obstacles in front of it. Please verify the infrared sensor value with the serial monitor.**

**Milestone 2.2: Your robot should be able to stop in front of any obstacle without hitting it. The robot should start moving again after the obstable clears.**

**Milestone 2.3: Your robot should be able to adjust its speed based on its distance to a moving obstacle in front of it. Your robot should move faster if the obstacle accelerates and move slower if the obstacle deccelerates.**

### Task 3: Aligning the drive path

As you may have noticed from Lab 2, the robot may not drive in a straight line even if you set the same speed for both motors due to variation on the condition and power of the motors. Therefore, you should calibrate the speeds of the two wheels carefully so that the robot will move in a straight line. We will be setting up a straight track in which multiple robots are expected to move forward one after another in a single file without bumping into each other and without lagging behind. If your robot is able to move relatively straight, it will also minimize the chance of bumping into the wall on either side of the track. However, it may be difficult to keep the robot in a straight line all the time due to unpredictable variations in the hardware. Therefore, you should also take advantage of the bumpers to detect any wall and adjust the direction of the robot accordingly so it reverts to a more straight path following the track. The goal is to minimize the chance of crashing into the walls of the track to reduce congestion in the track with other robots.

**Milestone 3.1: Your robot should be able to move in relatively straight line (without bumping into the track for at least 15 seconds).**

**Milestone 3.2: Your robot should be able recover a straigh path after bumping into any wall in the track. Your robot should be able to move from one end of the track to the other end without creating congestion that prevents other robots from moving.**

### Putting everything together

Combine the functionalities created for the robots in the previous three tasks into a single robot that contains all these functionalities in one. This involves integrating the three pieces of Arduino code into one piece of code and uploading it into the Seeeduino micro-controller. Afterward, you will use a Seeeduino stacked with motor shield and maker shield to control your final integrated robot.

**Milestone: You should test whether the integrated robot can accomplish the goals defined in all previous milestones.**
  
**Milestone: Find another finished group and see if you can get one robot to adjust its speed depending on a second robot in front of it. Line your two robots up and simply control the speed of the leading robot using the digit recognition system.  See if you can get the trailing robot to dynamically adjust its speed to avoid collision.**
