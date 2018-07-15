Communication Tutorial
=======================

This tutorial will walk you through the necessary steps to allow your robot to connect to the Internet.  We will be using the same robots as in Lab 2 as well as an additional Adafruit Wifi board. In order to accomodate this Wifi board, you will need to make some modifications to your robot's hardware.  This will allow the Wifi board to properly connect to the Arduino, making it possible for your robot to communicate with the digit recognication web application you used in Lab 3. Following this hardware modification, you will then need to upload new software to your robot's Arduino that allows it to establish a connection with our server. At the end of this tutorial, your robot should be able to receive information over the Internet, and you can move on to creating your adaptive cruise control system!

### Hardware Modification 
Previously in Lab 2, you used a robot controlled by a board stack consisting of an Arduino and two additional shields.  These shields work by plugging into designated pins in the bottom Arduino board.  The motor shield, which controls the two drive motors of the robot, currently utilizes 8 pins on the bottom Arduino (pins A0, A1, D3, D8, D9, D10, D11, D12, and D13).  Several of these pins operate as both simple digital input/output pins and special types of pins used for a communication interface called Serial Peripheral Interface (SPI).  The motor shield simply requires several digital input/output pins and does not need SPI functionality, but the Wifi board we are using uses SPI to communicate with the Arduino.  For this reason, we will be separating our circuit board stack and externally connecting the motor shield and the Wifi board to the Arduino using wires.  This will allow us to connect the motor shield to different pins, freeing up the specialized SPI pins needed for our Wifi board. 

The current circuit board stack consists of a maker shield on top, followed by a motor shield in the middle and an Arduino board on the bottom.  First, disconnect all three boards by carefully pulling them apart.  Mount the maker shield directly onto the Arduino board.  A small breadboard mounted on a clear plastic plate will be used to connect the motor shield and the Wifi board. Without removing any wires from the Motor shield, connect the pins on one side of the board to the first lettered column on the breadboard (not a column labeled + or -) so that the pins on the opposite side are disconnected from the breadboard and the last pin of the motor shield is in row 18 of the breadboard. Connect the connectors of the motor shield to the connectors of the maker shield using long wires according to the pinout table below. 

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

### Software Setup 
In your final project, your robot will be communicating with our server via a router. Each Wifi board has been assigned and bound to its own unique IP address. Each board will also utilize its own distinct port. In this way, a predicted number from the digit recognition site can be sent from the server to the router, which can then send the same number to your individual Wifi board. To establish this connection using an Arduino, we have provided code that connects your Wifi board to the network and provides useful checks for you in the Arduino IDE's serial monitor. The first portion of the code establishes a connection to the network and prints connection details in your serial monitor. The second part of the code contains the loop that continuously checks for available data. Once the digit recognition server returns a predicted digit, this number will be sent to your Arduino and stored in the variable 'value'.  When utilizing this code, you will need to change the LISTEN_PORT number to your group number in order to connect to the correct port. It is also important that you ensure you are logged into your group's account on the digit recognition server as this allows your board to have its own, distinct connection.  Once you have changed the LISTEN_PORT number and uploaded the code to your robot, open your serial monitor to check that your device has successfully connected to the network.  Test this system by logging into the digit recognition site, uploading your code from Lab 3, and drawing a digit to predict.  This digit should then be printed out in your Arduino IDE's serial monitor. You will now be able to recieve digit recognition numbers and can go on to implement digit-dependent robot motion. 
