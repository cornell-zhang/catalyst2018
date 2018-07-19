
# Project 1: Rapid Targeting System 

### Goal 

Use the robot to more rapidly navigate a maze and reach the target using various sensors. We will have a competition between groups to see which robot can navigate the maze the fastest. You are allowed to use all sensors installed on the robot and read their values to help you accomplish this task. If you have forgotten which sensors are on the robot, you may review the handout for Lab 2 for a diagram of the sensors on the robot. Some of these sensors were not used in either Lab 2 and Lab 3.

The maze you will be navigating in this project is the same one that you had used in Lab 2. The robot will start at a randomly chosen position on the opposite side of the wall from the target. Each time before starting, it will spin some number of degrees according to the number you write on your digit recognition web app. We will provide more detail about how you should have your robot spin later on in this handout. We may add more obstacles to the course in order to test the robustness of your robot intelligence. We can also change the starting location of the robot.

This project can be divided into independent tasks. Each group should further divide into subgroups to work on different tasks in parallel. At the end, different subgroups will come together to assemble the final system. Each group will get multiple robots to experiment with their design so that each subgroup has its own robot to work with.

### Task 1: Setting up the wireless communication

In order to allow the robot to receive a digit from the digit recognition web app, we will need to enable wireless connectivity on the robot by integrating a WiFi chip into the design. Specifically, we will wire up the CC3000 WiFi board on a breadboard on the side of the Arduino stack and connect the WiFi board to the appropriate pins on the Arduino stack. Please refer to the [Arduino Uno Communication Tutorial](../Communication%20Tutorial/Uno) for detailed instructions on how to set up the pin connections and build the hardware.

Once the hardware is all wired up, you will need to program the software to make use of the WiFi board. For this part, you will first study our [code template](../Communication%20Tutorial/Uno#part-2software-setup) and then integrate it into the program for your robot to receive digit from the web app.

Once your robot can successfully receive a digit from the web app, you can program your robot to spin based on the value of the digit. Please note that the digit will be use to determine the initial orientation of the robot, and this orientation affects the direction for which the robot is initially facing and thus how fast it can get to the target. Therefore, be sure to determine the mapping between digit and rotation angle carefully and convey this information to anyone who would be starting the robot.

**Milestone 1.1: Your robot should be able to receive any digit sent from our digit recognition web app. You should verify the received digit with the serial monitor.**

**Milestone 1.2: Your robot should be able rotate for a certain number of degrees based on the value of the digit sent from the web app. For example, your motors should rotate 30 degrees for every increment in the digit.**

### Task 2: Developing smart wandering behaviors

We will make use of various sensors (infrared sensor, greyscale sensor, bumpers) to increase the speed at which the robot navigates the maze and reach its final destimation. As part of the this process, you should think of how the robot should react to different values from these sensors. For example, which direction should it turn when a left bumper is hit versus when a right bumper is triggered? Can you also look at the signal from the infrared sensor to more intelligent determine how to turn? How general are the optimizations that you implement? For the design of your robot, can it handle different maze configurations? For your robot, are there any design tradeoff between having a fixed maze versus a dynamically reconfigurable maze? As in Lab 2, when the robot reaches the target, it should spin 360 degrees and stop moving.

##### Design tips

1. To help improve navigation time, you can increase the speed of the motors so that the robot can move and turn faster. However, the robot will be less stable and will likely tip over. You will therefore need to adjust the speed enough, so that you have a combination of speed and stability. The only way to do this, is to test your design multiple times and adjust the speed accordingly.
2. The infrared sensor in the front can be used to sense distance between the sensor and the wall. It is recommended that you utilize the front infrared sensor to allow the robot to see the distance between itself and the wall; think about how the robot will know (or can guess) that it is going the right way. The front infrared sensor can also prevent the robot from getting stuck. The front facing infrared sensor will be useful for getting the robot out corners where bumpers can't detect.  
3. The bumpers are an excellent tool to provide information to the robot. You may refer to the Lab 2 handout to see how you can use the bumper information to get your robot to navigate faster through the maze.

**Milestone 2.1: Demonstrate one new feature implemented in your robot that allows it to reach the target faster. Make sure you can articulate why this new feature is useful. You will be required to demonstrate and time both your old robot and new robot in the maze.**

**Milestone 2.2: Demonstrate another new feature implemented in your robot that allows it to reach the target faster. Please also articulate why this new feature is useful.**

### Putting everything together

After the two subgroups have finished their respective parts, you should integrate the two parts together into one, single piece of Arduino code that you can upload to the robot and have it meet the specifications we have just listed. This involves integrating the three pieces of Arduino code into one piece of code.

**Milestone: You should test whether the integrated robot can accomplish the goals defined in all previous milestones.**

**Milestone: Find another finished group and see how your robot competes against the robot of the other group. Discuss your designs and make the appropriate improvements.**





