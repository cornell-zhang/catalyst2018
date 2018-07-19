Communication Tutorial
=======================

This tutorial will walk you through the necessary steps to allow your robot to connect to the Internet.  We will be using the same robots as in Lab 2 as well as an additional Adafruit CC3000 Wifi board (Figure 1). 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Uno/figures/CC3000.PNG" width="300">
    <font size="2">
    <figcaption> Figure 1: CC3000 WiFi board  <br><br></a> 
    </figcaption>
    </font>
</figure>

In order to accomodate this Wifi board, you will need to make some modifications to your robot's hardware. This will allow the Wifi board to properly connect to the Arduino, making it possible for your robot to communicate with the digit recognication web application you used in Lab 3. Following this hardware modification, you will then need to upload new software to your robot's Arduino that allows it to establish a connection with our server. At the end of this tutorial, your robot should be able to receive information over the Internet, and you can move on to creating your adaptive cruise control system!

### Part 1.Hardware Modification 
Previously in Lab 2, you used a robot controlled by a board stack consisting of an Arduino and two additional shields. The Uno is the microcontroller in the bottom, and the motor shield is in the middle which is applied to control the motors, and the maker is on the top which is used to connected with other necessary components including LEDs, grayscale sensors, infrared sensors, etc. Figure 2 shows the pin connection of Arduino UNO.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Uno/figures/UNO_pin.png" width="800">
    <font size="2">
    <figcaption> Figure 2: Pin connection of Arduino UNO  <br><br></a> 
    </figcaption>
    </font>
</figure>

Both motor shield and maker shield work by plugging into designated pins in the bottom Arduino board. The motor shield, which controls the two drive motors of the robot, currently utilizes 8 pins on the bottom Arduino (A means Analog; D means Digital; pins A0, A1, D3, D8, D9, D10, D11, D12, and D13).  Several of these pins operate as both simple digital input/output pins and special types of pins used for a communication interface called Serial Peripheral Interface (SPI).  The motor shield simply requires several digital input/output pins and does not need SPI functionality, but the Wifi board we are using uses SPI (pin number D11, D12, and D13) to communicate with the Arduino.  For this reason, we will be separating our circuit board stack and externally connecting the motor shield and the Wifi board to the Arduino using wires.  This will allow us to connect the motor shield to different pins, freeing up the specialized SPI pins needed for our Wifi board. 

Again, the current circuit board stack consists of a maker shield on top, followed by a motor shield in the middle and an Arduino UNO board on the bottom.  First, disconnect all three boards by carefully pulling them apart.  Mount the maker shield directly onto the Arduino board.  A small breadboard mounted on a clear plastic plate will be used to connect the motor shield and the Wifi board. Without removing any wires from the Motor shield, connect the pins on one side of the board to the first lettered column on the breadboard (not a column labeled + or -) so that the pins on the opposite side are disconnected from the breadboard and the last pin of the motor shield is in row 18 of the breadboard. Connect the connectors of the motor shield to the connectors of the maker shield using long wires according to the pinout table below. 

|Motor Shield Pin | Maker Shield Pin|
|---------------- |-----------------|
|reset            |rst              |
|3.3V             |-                |
|5V               |3V3              |
|GND              |GND              |
|GND              |-                |
|Vin              |-                |
|PWM A 3          |D3               |
|PWM B 11         |D9               |
|DIR A 12         |D5*              |
|DIR B 13         |D10              |

* In order to attach a wire from pin DIR A 12 to pin to D5 you can completely remove the existing wire connected to pin D5. This connection was previously used to control the board LED and will not be needed for the final project.

Next, attach the Wifi board to the breadboard so that its row of pins are connected to column i of the breadboard. Use the two breadboard columns above the board to make connections between the Wifi Board and the maker shield according to the table below. 

|Wifi Board Pin | Maker Shield Pin|
|---------------|-----------------|
|IRQ            |D2               |
|VBEN           |D4               |
|CS             |D8               |
|MOSI           |D11              |
|MISO           |D12              |
|CLK            |D13              |
|VIN            |-                |
|3V3            |-                |
|GND            |-                |

Connect the VIN pin on the Wifi board and the 5V pin on the maker shield to pins in the + column of the breadboard. Then, connect the GND pin on the Wifi board and the GND pin on the maker shield to pins in the - column of the breadboard. 

The hardware setup for your robot should now be complete!

### Part 2.Software Setup 
In your final project, your robot will be communicating with our server via a router. Each Wifi board has been assigned and bound to its own unique IP address. Each board will also utilize its own distinct connection port. In this way, a predicted number from the digit recognition site can be sent from the server to the router, which can then send the same number to your individual Wifi board. The following figure shows the Correspondence among CC3000 label, connection port number, and group number. You will find the CC3000 label in the bottom of the plastic plate. The group number is used for login the Digit Recognition System you have experienced in lab 3. Please open "Chrome" and type in the IP address “132.236.59.106” or the domain name "zhang-precision-02.ece.cornell.edu" to access our server. According to your group number, your username will be "gX", where "X" is your group number.

|CC3000 Label   |Port #           |Group #        |
|---------------|-----------------|---------------|
|A              |10               |10             |
|B              |11               |11             |
|C              |12               |12             |
|D              |13               |13             |
|E              |14               |14             |


To establish this connection using an Arduino, we have provided code (snapshot) that connects your CC3000 Wifi board to the network and provides useful checks for you in the Arduino Wed Editor's serial monitor. The first portion of the code establishes a connection to the network and prints connection details in your serial monitor. The second part of the code is the initial configuration, and the final part contains the loop that continuously checks for available data. To get started, please open the Arduino Web Edidor you used in lab2, create a new sketch and type in the following code (Figure 3,4,5).
Attention: Please remember to change the LISTEN_PORT number to your own one.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Uno/figures/s1.PNG" width="800">
    <font size="2">
    <figcaption> Figure 3: Include necessary libraries, Pin connection, and variable definition.   <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Uno/figures/s2.PNG" width="800">
    <font size="2">
    <figcaption> Figure 4: Initial Setup.   <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/projects/Communication Tutorial/Uno/figures/s3.PNG" width="800">
    <font size="2">
    <figcaption> Figure 5: Main loop and print helper function.   <br><br></a> 
    </figcaption>
    </font>
</figure>

Once the digit recognition server returns a predicted digit, this number will be sent to your Arduino and stored in the variable 'value'.  When utilizing this code, you will need to change the LISTEN_PORT number to your group number in order to connect to the correct port. It is also important that you ensure you are logged into the correct group account on the Digit Recognition System as this allows your board to have its own, distinct connection. The information is in a table with the CC3000 label, Port and Group numbers below. Again, make sure you have changed the LISTEN_PORT number and uploaded the code to your robot, open your serial monitor to check that your device has successfully connected to the network.  Test this system by logging into the Digit Recognition System, and drawing a digit to predict. This digit should then be printed out in your Arduino Wed Editor's serial monitor. You will now be able to recieve digit recognition numbers and can go on to implement digit-dependent robot motion. 

