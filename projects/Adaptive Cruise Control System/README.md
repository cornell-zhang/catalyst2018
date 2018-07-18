Project 2: Adaptive Cruise Control System
======================
In this project, you will equip your robot with an adaptive cruise control system and install a remote control mechanism that will allow you to control the speed of your robot using the digit recognition system implemented in Lab 3. An adaptive cruise control system automatically regulates the distance between a car and other cars and obstacles. This system adapts the speed of the car based on its distance to other cars and objects, and serves as the the basis for making "smart" self-driving cars. 

In this lab, you will implement a version of an adaptive cruise control system, albeit one that's much simpler than those used in self-driving systems. While there are many possible features that you can implement, as the core of this project, you will use the infrared sensor attached to detect the distance between your robot and any obstacle that may be in front of it. Based on the distance to the nearest obstacle in front of it, you should make your robot change speeds accordingly. To implement remote control, we will provide you with a code template for connecting your robot to the WiFi after minimal amount of rewiring. This will allow you to control your robot by drawing digits on the canvas from Lab 3.

This project can be divided into independent tasks. Each group should further divide into subgroups to work on different tasks in parallel. At the end, different subgroups will come together to assemble the final system. Each group will get multiple robots to experiment with their design so that each subgroup has its own robot to work with.

### Task 1: Setting up the wireless connection
For this final project, your robots will need to have Internet connection capabilities.  For this reason, we will be using a different type of board in place of the Arduino Uno you previously used. We will be using a Seeeduino board, which has an integrated Wifi chip. Once your group has received a Seeeduino, please carefully remove the Arduino Uno from the bottom of your robot's circuit board stack, and plug in the Seeeduino instead. The Seeeduino should be able to attach to the board stack in the same manner as the Arduino Uno. Please take extra precaution when aligning the pins so that pins do not get bent and damaged. 

When using the Arduino web editor to program your robot, you will need to change the board type. Select the drop-down bar at the top that currently reads "Arduino Uno" then click "Select Other Board & Port."  Choose the "Arduino Yun" option. To allow each group to simultaneously use the digit recognition web server to control their robot, each group must connect to a different port. Each Seeeduino board has a unique MAC address and has been bound to a specific port in our router. When using our code template, be sure to locate the `#define PORT #` line and change the number to your group number. When signing in to the digit rec web server, you should also be sure to sign into the account corresponding to your correct group number. Specific instructions on the WiFi connection and port numbers are provided as part of the [Seeeduino communication tutorial](../Communication%20Tutorial/Seeeduino). Please carefully read this tutorial before completing the task. You can find the port that you will have to change to, along with the appropriate group number, by referring to the table that in the communication tutorial.

### Task 2: Developing the cruise control system 
You should first develop and test just your cruise control system. Determine a function that will relate your desired speed with distance values received from the infrared value. Your speed value should have an inverse relationship with distance, as your robot should drive slowly when near objects and drive at a faster speed when far away from objects.  Speeds should range from 0 to approximately 125 in order to ensure that the robot does not drive at an unreasonably fast speed.  You might find it helpful to first print out distance values from the infrared sensor over the serial monitor in order to determine the range of distance values.  If you forget how to print out values over the serial monitor, feel free to reference your code from Lab 2 (the grayscale sensor code might be helpful).  Hint: be sure that your loop function continuously reads infrared sensor values, uses your previous function to determine a speed based on this distance value, and sets the speed-controlling pins of the Arduino to these values.  Test your cruise control system by uploading it to the robot and seeing if you can observe a noticeable difference in speed when you move your hand closer to the robot. 

Once you have developed a successful cruise control system, you can create the FSM that will allow your robot to use the cruise control system and the digit recognition system.  It might be helpful to use a new copy of the template code for this. Your FSM should be simple, containing three different states: a state in which your robot moves forward with a speed that depends on the infrared sensor, a state in which your robot moves forward with a speed that depends on the number received from the digit recognition system, and a stop state. For organizational purposes, you should write each of these states as a separate function.  To implement the function for the cruise control state, you can simply copy the code you previously wrote. A `receive_value` function has been provided for you.  This function simply reads the digit received over WiFi from the web server and stores it in a variable `value`. You should then create a function that determines the next state based on the variable `value`. This function should also use the `receive_value` function to first read values received from the server. The next important function you should write is one that switches the robot's state, depending on the next state determined by the function you previously wrote.  Hint: do not forget to define all variables you use at the beginning of your code! Your loop function should continuously determine the next state and switch the robot to this state, using the two functions you just wrote. 

Notes on Coding: 
In your function that determines the next state, you will want to set a new variable `state`, depending on `value`.  You should use `if...else` conditionals for this.  
In your function that switches your robot's state, you will want to use something called `switch`.  The syntax for this is show below: 
```
switch(variable)
{
  case 0:
    function1();
    break;
  case 1: 
    function2();
    break;
  default: 
    function3();
  }
  ```
  In this example case, if `variable` is 0, function1() will be executed and if `variable` is 1 function2() will be executed.  By         default, function3() will be implemented. You will need to use a similar format for implementing your function to switch FSM states.
  
### Part 3: Testing Your Adaptive Cruise Control System
After compiling and uploading your code to the robot, test your robot on the testing block to ensure that it adjusts its speed depending on the distance of your hand in front of it.  Once the cruise control system is working, test the digit recognition control system. Write numbers on the digit rec server and make sure that your robot adjusts its speed depending on the predicted number. You can then place your robot on the ground and further test its cruise control system by placing objects in front of it.  

As a further challenge, find another finished group and see if you can get one robot to adjust its speed depending on a second robot in front of it. Line your two robots up and simply control the speed of the leading robot using the digit recognition system.  See if you can get the trailing robot to dynamically adjust its speed to avoid collision. 
  
Note: If you find that your robots are not driving in entirely straight lines, you will need to manually tune the wheel speeds to fix this issue. Test to see which way your robot is drifting to, and subtract or add a small integer to one of the wheel speeds in the code. Keep adjusting these integers until your robot drives forward in a straight line. 
