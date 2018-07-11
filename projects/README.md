Projects
======================

Intelligent electronic systems are broadly applied in many applications including in IoT devices and auto-driving systems.  For the final project, you are going to choose one of the following two competitions.

Proposals
--------------------------------

### 1. Rapid Targeting System:
In this competition, students will build a robot which is able to quickly arrive at the destination. You should use the digit recognition system built in lab3 to start the robot.  For instance, if you draw the number “5” on the canvas, the predicting result should be “5” and it will be sent to the robot, the robot will start targeting the destination after spinning around 5 times. You should teach the robot how to rapidly find the destination.

### 2. Adaptive Cruise System:
In this competition, students will build a robot equipped with an adaptive cruise system. Adaptive cruise control systems are used by many modern vehicles to avoid collisions by automatically adjusting their speed depending on their distance to objects. Students will attempt to model this system by programming their robots to adjust their speed based on values recieved from an infrared sensor. This should allow several robots with varying speeds to drive in a straight line without colliding. To allow for control of the robot while in motion, students will also implement a control system based on the digit recognition system used in Lab 3.  This will utilize the same web server to predict a digit based on a hand-drawn number, which will be used to communicate with and control the robot.  For instance, if the number "1" is drawn in the web server canvas, the digit recognition system should predict "1," this number should be sent to the robot, and the robot should slow down. This will require students to also implement Wifi communication capabilities in their robots. Ultimately, students should be able to control one robot using the digit recognition system and have another robot trail behind, automatically adjusting its speed to avoid collision. 
