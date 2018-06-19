Projects
======================

Intelligent electronic systems are broadly used in many applications including smart house, health monitor, and auto-control systems. To further explore the digital intelligence, you will build an intelligent system by implementing simple machine learning algorithms like KNN, linear regression, and decision tree. You should first collect some data and train your model, then verify its functionality, and finally display the classification/prediction on the TFT screen or use it to control the robot.

Proposals
--------------------------------

### 1. Digit Recognition:
In this project, students will build a more powerful integrated digit recognition system, which is able to apply the IoT box to check the predictions. Based on the web-based digit recognition system built in lab3, you should implement a chat channel between the server and an Arduino-embedded IoT box so that it could receive the predicting result and display it on the TFT screen.

### 2. Dancing Robot:
In this project, students will build a dancing robot, which is remotely controlled by drawing numbers on the canvas used in lab3. Based on the web-based digit recognition system built in lab3, you should implement a chat channel between the server and an Arduino-embedded IoT box so that it could receive the predicting result and use the corresponding value to control the moving pattern of a robot built in lab2. For instance, if you draw a “0” on the canvas, after prediction, the robot will move forward for a while.

### 3. Motion predictor:
In this project, students will build a motion predictor to detect and predict the user’s current and future activity. Users’ will wear the sensor called ADXL335 Accelerometer on the arm or put it in the pocket. The output values from the sensor are proportional to the acceleration in the x, y, and z directions, which could be used to prediction the user’s motion. You could use a decision tree to classify user’s motion. Three basic moving patterns could be still, walk, and run. As for motion prediction, you could refer to the time. For example, in the morning, if one user walks for 15 to 20 minutes, and then stay still for a longer time, say 1 hour, he/she may start work and there is a high probability that he/she will keep working (stay still) until noon.

### 4. Electronic doctor:
In this project, students will build an electronic doctor who will measure users’ heartbeat rate, and provide the professional diagnosis. You will use the D9 Neosid Heartbeat Sensor to measure the heartbeat rate. Also, your smart system should be able to detect athlete and users who did some strenuous exercise just now. A decision tree is a suitable machine learning algorithm for this design.

https://www.google.com/imgres?imgurl=https://www.health.harvard.edu/media/content/images/average-heart-rate.png&imgrefurl=https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you&h=465&w=376&tbnid=WK0P6J7R9RM9hM:&q=normal+heart+rate&tbnh=160&tbnw=129&usg=__JGoT6nf0IW8vixDVe3kSs6LqyzI%3D&vet=1&docid=Hd80ZZ_S4slVoM&client=chrome-omni&sa=X&sqi=2&ved=0ahUKEwjGmKL37N_bAhVHCjQIHaaJC1QQ9QEILTAA#h=465&imgdii=WK0P6J7R9RM9hM:&tbnh=160&tbnw=129&vet=1&w=376

### 5. Finger-controlled robot:
In this project, students will build a robot whose motion is controlled by one finger. You should use the force sensor and decision tree/linear regression to build the system. For instance, if you press the force sensor in a light way, the robot will move forward; if you press heavily on the force sensor, the robot will move backward; and if you don't press the force sensor, the robot will stay still.

### 6. Color recognition:
In this project, students will train a robot to recognize different colors. You should use the grayscale sensor in the bottom of the robot and decision tree/linear regression to build the system. 

### 7. Mini-autodrive system:
In this project, students will build a smart robot who is able to drive safely in the lab. You should use the infrared sensor in the front of the robot and decision tree/linear regression to build the system. The Basic idea is to avoid any collision during the auto-driving.



