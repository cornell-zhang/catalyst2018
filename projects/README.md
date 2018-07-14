Projects
======================

Intelligent electronic systems are broadly applied in many applications including in IoT devices and auto-driving systems.  For the final project, you are going to choose one of the following two competitions.

Proposals
--------------------------------

### [1. Rapid Targeting System](Rapid%20Targeting%20System)
In this competition, students will build a robot that is able to quickly arrive at its destination. Students will use the same wooden maze as in Lab 2, but should implement more sophisticated programs that allow the robots to reach their targets in much shorter periods of time. Programs should include infrared mapping, which allow the robot to determine the direction in which the object directly ahead is the furthest away. This should allow the robot to determine the shortest route to the target from its current position.  As an additional challenge, students will develop a way to change the starting orientation of the robot by directing it to spin a certain number of degrees using the digit recognition system from Lab 3. Students should use WiFi communication to send a digit to the robot, causing it to rotate for a specified amount of time. After changing its starting orientation by rotating, the robot should proceed to rapidly navigate the maze to reach its target.


### [2. Adaptive Cruise System](Adaptive%20Cruise%20Control%20System)
In this competition, students will build a robot equipped with an adaptive cruise system. Adaptive cruise control systems are used by many modern vehicles to avoid collisions by automatically adjusting their speed depending on their distance to objects. Students will attempt to model this system by programming their robots to adjust their speed based on values recieved from an infrared sensor. This should allow several robots with varying speeds to drive in a straight line without colliding. To allow for control of the robot while in motion, students will also implement a control system based on the digit recognition system used in Lab 3.  This will utilize the same web server to predict a digit based on a hand-drawn number, which will be used to communicate with and control the robot.  For instance, if the number "1" is drawn in the web server canvas, the digit recognition system should predict "1," this number should be sent to the robot, and the robot should slow down. This will require students to also implement WiFi communication capabilities in their robots. Ultimately, students should be able to control one robot using the digit recognition system and have another robot trail behind, automatically adjusting its speed to avoid collision. 
