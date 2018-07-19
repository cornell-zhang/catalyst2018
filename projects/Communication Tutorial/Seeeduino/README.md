Communication Tutorial
---

In this tutorial, you will learn how you can use WiFi to communicate with your Seeeduino Cloud. The reason we will be using the Seeeduino Cloud as opposed to the Arduino Uno, is that the only way you can use WiFi with an Uno is if you use an external WiFi chip(like we are doing in the first tutorial). The WiFi chip we are using, the CC3000, however, is very sensitive, and so it won't work when you turn the motors of your robot on. For this reason, if you have chosen to do project 2, we have chosen to use the Seeeduino Cloud, which contains its very own WiFi module, that isn't as sensitive as the CC3000. You should note that the Seeeduino Cloud (Figure 1) is compatible with the Arduino Yun, which is a discontinued series of the Arduino line. Since it's discontinued, however, we had no way to get a hold of them, so we will use the Seeeduino Cloud instead, for this project.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Seeeduino/figures/seeeduino.PNG" width="400">
    <font size="2">
    <figcaption> Figure 1: Seeeduino Cloud  <br><br></a> 
    </figcaption>
    </font>
</figure>

For more information about Seeeduino Cloud, please visit this website:
<a href="http://wiki.seeedstudio.com/Seeeduino_Cloud/"> Seeeduino Cloud Wiki </a> 

### Part 1.Hardware Modification
To start, you will first need the necessary materials, which include a robot and a Seeeduino Cloud. When you get your Seeeduino, you will want to note down the label that's on the side of it, as it will be necessary later on. When you get your robot, you will find that the Arduino Uno is still at the bottom of the circuit stack, on top of the robot. So that we can use the WiFi module from the Seeeduino, while keeping the other robot functionality the same as in lab 2, you will have to unplug the Arduino Uno from the bottom of the circuit stack, and replace it with the Seeeduino Cloud. Make sure that when you plug in the Seeeduino Cloud, you aren't bending any pins away from their respective sockets. If you end up making this mistake, you may find that some parts of your robot aren't working, as not all the signals from the Seeeduino Cloud will be sent to the rest of the circuit stack. 

### Part 2.Software Setup
In your final project, your robot will be communicating with our server via a router. Each Seeeduino has been assigned and bound to its own unique IP address. Each board will also utilize its own distinct connection port. In this way, a predicted number from the digit recognition site can be sent from the server to the router, which can then send the same number to your individual Seeeduino. The following figure shows the Correspondence among Seeedunio Cloud label, connection port number, and group number. You will find the Seeeduino label in the side of the pins. The group number is used for login the Digit Recognition System you have experienced in lab 3. Please open "Chrome" and type in the IP address “132.236.59.106” or the domain name "zhang-precision-02.ece.cornell.edu" to access our server. According to your group number, your username will be "gX", where "X" is your group number.

|Seeeduino Cloud Label | Port # | Group # |
|----------------------|--------|---------|
|1                     |1       |1        |
|2                     |2       |2        |
|3                     |3       |3        |
|4                     |4       |4        |
|5                     |5       |5        |

To establish the connection using a Seeeduino, we have provided code (snapshot: Figure 2,3,4) that connects your Seeeduino to the network and provides useful checks for you in the Arduino Wed Editor's serial monitor. Since the Seeeduino is compatible with Arduino Yun, it will be recognized as Arduino Yun when you connect the Seeeduino with the computer. The first portion of the code establishes a connection to the network and prints connection details in your serial monitor. The second part of the code contains the loop that continuously checks for available data. To get started, please open the Arduino Web Edidor you used in lab2, create a new sketch and type in the following code (Figure 2,3). Attention: Please remember to change the LISTEN_PORT number to your own one.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Seeeduino/figures/s1.PNG" width="800">
    <font size="2">
    <figcaption> Figure 2: Include necessary libraries, Pin connection, and variable definition. And Initial Setup.  <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Seeeduino/figures/s2.PNG" width="800">
    <font size="2">
    <figcaption> Figure 3: Main loop. <br><br></a> 
    </figcaption>
    </font>
</figure>

Once the digit recognition server returns a predicted digit, this number will be sent to your seeeduino and stored in the variable 'value'. When utilizing this code, you will need to change the LISTEN_PORT number to your group number in order to connect to the correct port. It is also important that you ensure you are logged into the correct group account on the Digit Recognition System as this allows your board to have its own, distinct connection. The information is in a table with the CC3000 label, Port and Group numbers below. Again, make sure you have changed the LISTEN_PORT number and uploaded the code to your robot, open your serial monitor to check that your device has successfully connected to the network. Test this system by logging into the Digit Recognition System, and drawing a digit to predict. This digit should then be printed out in your Arduino Wed Editor's serial monitor. You will now be able to recieve digit recognition numbers and can go on to implement digit-dependent robot motion.
