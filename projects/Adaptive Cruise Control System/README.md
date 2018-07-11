Project 2: Adaptive Cruise Control System
======================
In this project, you will equip your robot with an adaptive cruise control system, and also add functionality that will let you control the speed of your robot using the digitrec system that you implemented in Lab 3. So what exactly is an adaptive cruise control system? Recently, we have made many advances in the automotive industry, with Google and other companies coming out with things like self-driving cars. These cars, in order to avoid crashes and to abide by the laws of the road, will implement an adaptive cruise control system, so that they put enough distance between themselves and other cars/obstacles. The adaptive cruise control system is the basis for making these cars "smart".

In this lab, you will implement a version of an adaptive cruise control system, albeit one that's much simpler than those used in self-driving cars. You will use the infrared sensor sitting at the front of the robot to detect the distance between your robot and any obstacle that may be in front of it. Based on the distance to the nearest obstacle in front of it, you should make your robot change speeds accordingly. It may be helpful for you to build an Finite-State Machine(FSM) before you begin, so that you can capture the logic you will be using, and have a much easier time implementing your code. We will provide you with some example code on how your robot can connect with the WiFi(you will also have to adjust the wiring of the robot, so that you can add in the WiFi card), so that you will also be able to control your robot by drawing digits on the canvas(which you will be able to access in the same way you did in lab 3). Lastly, we will simplify this system even further by mandating that your robot travels as straight as possible. When you are testing this, you will find that your robot will likely curve to the side, since one wheel is likely more sensitive to speed increases than the other. To fix this, you will have to adjust the speed of one of the wheels, so that your robot will always travel in a straight line.

### Part 1: Wiring the Robot


### Part 2: Developing the Code 
You should first develop and test just your cruise control system. Determine a function that will relate your desired speed with distance values recieved from the infrared value. Your speed value should have an inverse relationship with distance, as your robot should drive slowly when near objects and drive at a faster speed when far away from objects.  Speeds should range from 0 to approximately 125 in order to ensure that the robot does not drive at an unreasonably fast speed.  You might find it helpful to first print out distance values from the infrared sensor over the serial monitor in order to determine the range of distance values.  If you forget how to print out values over the serial monitor, feel free to reference your code from Lab 2 (the grayscale sensor code might be helpful).  Hint: be sure that your loop function continuously reads infrared sensor values, uses your previous function to determine a speed based on this distance value, and sets the speed-controlling pins of Arduino to these values.  Test your cruise control system by uploading it to the robot and seeing if you can observe a noticeable difference in speed when you move your hand closer to the robot. 

Once you have developed a successful cruise control system, you can create the FSM that will allow your robot to use the cruise control system and the digit recognition system.  Your FSM should be simple, containing three different states: a state in which your robot moves forward with a speed that depends on the infrared sensor, a state in which your robot moves forward with a speed that depends on the number received from the digit recognition system, and a stop state. For organizational purposes, you should write each of these states as a separate function.  To implement the function for the cruise control state, you can simply copy the code you previously wrote. A `receive_value` function has been provided for you.  This function simply reads the digit received over WiFi from the web server and stores it in a variable `value`. You should then create a function that determines the next state based on the variable `value`. This function should also use the `receive_value` function to first read values received from the server. The next important function you should write is one that switches the robot's state, depending on the next state determined by the function you previously wrote.  Hint: do not forget to define all variables you use at the beginning of your code! Your loop function should continuously determine the next state and switch the robot to this state, using the two functions you just wrote. 

Notes on Coding: 
-In your function that determines the next state, you will want to set a new variable `state`, depending on `value`.  You should use `if...else` conditionals for this 
-In your function that switches your robot's state, you will want to use something called `switch`.  The syntax for this is show below: 
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
  In this example case, if `variable` is 0, function1() will be executed and if `variable` is 1 function2() will be implemented.  By         default, function3() will be implemented. You will need to use a similar format for implementing your function to switch FSM states. 
