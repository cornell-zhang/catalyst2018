Lab 1: Mystery Circuit
======================

In this first lab assignment, both you and your partner will experiment with basic circuit components, gradually building your way up into building a two-bit ripple-carry adder. In the first section, you will experiment with both basic analog and digital circuits, culminating with the creation of a NAND gate. In the second part, you will experiment with basic logic gates, and eventually develop a parity checker. In the last part, you will use everything you have learned thus far to incrementally build a two-bit ripple-carry adder. After finishing each section, make sure that a teaching assistant verifies the correct outcome and initials the appropriate line on the sign-off sheet. **Make sure to turn in your sign-off sheet by the end of the lab session.**


Hardware Description
--------------------------------

Notice that we have given you not just a breadboard, but also some components that have already been wired up. You can verify that you aren’t missing any components on the breadboard by taking a look at Figure 1 below. You will also be able to use any of the supplies shown below in Figure 2. You should try to identify:
- PMOS and NMOS transistors 
- the LED 
- integrated circuits
- the digital input/output switches
- the breadboard power supply on your own prototyping platform. 
    
As for the other materials you will need, they are listed below:
- Black power cable with barrel connector
- LED
- Resistor
- Wire Cutter and Stripper


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagram.png" width="800">
    <font size="2">
    <figcaption> Figure 1: Simple LED Circuit Implemented on Prototyping Platform </a> 
    </figcaption>
    </font>
</figure>



<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/supplies1.jpg" width="200">
    <font size="2">
    <figcaption> Figure 2: Supplies </a> 
    </figcaption>
    </font>
</figure>

Lab Exercises
--------------------------

### Part 1. Understanding basic circuits
In this section, you will wire up some basic circuits that start with a simple analog LED circuit and then go to other simple digital circuits before going into developing a NAND gate. We will be exploring the basic building blocks that make up all electronics. A computer contains billions of transistors and logic gates such as the NAND gate are made up of these transistors. Inside a computer, there could be millions to billions of logic gates depending on the computer all working in conjunction to make the machine run. Understanding how these logic and basic circuit works is fundamental to understanding how a computer works. If you are ever in need of assistance, feel free to ask the TA’s for help. While you are wiring up circuits, make sure to turn OFF the breadboard power supply. Failure to do so may result in the circuit breaking. You may refer to Figure 3 below to see the wiring underlying the breadboard.


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardWiring.png" width="800">
    <font size="2">
    <figcaption> Figure 3: Underlying Wiring of Breadboard </a> 
    </figcaption>
    </font>
</figure>

Looking at figure 3, if we assume rows are denoted by number, we notice that all holes in a row are connected together. This means that any circuit components with both pins connected in the same rows are in parallel to each other. Different rows are not connected. Components with only one pin connected to the same row and the other pin connected to different rows are in series with each other. Components with no pins that share a row will not affect each other. The top and bottom of the figure shows the holes connected horizontally. These holes are typically for power and ground pins from the power source and circuit components 

#### Part 1.A Experiment with LED
LED stands for Light Emitting Diodes; a diode is a semiconductor device that allows current to flow easily in one direction but restricts current flowing in opposite direction. There are many different types of diode such as Zener Diode, which allows current to flow in the opposite direction if it reaches a certain voltage. Diodes can be used to protect motors and electronics from back current or current going in the reverse bias which can damage electronic components. The diode we are using provides light as the name suggests.
The circuit diagram shown in figure 5 contains three circuit components; the LED, which is the triangle with a line through it, the resistor, and the power source. The power source is denoted with a plus sign which shows the direction of current. Current always flow from high voltage to low voltage. Thus the current flows clockwise in the schematic. The LED must be placed in a specific direction for it to turn on. The two pins of the LED are cathode, the short pin, and the anode, the long pin. Look at the diagram in figure 4, the anode and cathode of the LED corresponds to its circuit representation. As current flows through the LED, it will emmit light.  

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LED.png" width="400">
    <font size="2">
    <figcaption> Figure 4: LED Schematic </a> 
    </figcaption>
    </font>
</figure>

Wire up the simple LED circuit shown in Figure 4 below. You may also refer to Figure 1, which shows the circuit wired up on the breadboard. Remember to place a resistor in the circuit. The LED does not have sufficient internal resistance to prevent short circuit. 
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LEDCircuitDiagram.png" width="200">
    <font size="2">
    <figcaption> Figure 4: Simple LED Circuit </a> 
    </figcaption>
    </font>
</figure>


```Sign-Off Milestone``` : Once you have wired everything up, have an instructor verify that the components are connected correctly; then the instructor will demonstrate how to plug in the barrel connector, test the circuit, and turn the board on/off using the switch on the breadboard power supply. Try putting the LED in both directions. 

*Critical Thinking Questions*: What do you think would happen if we used a resistor with higher resistance? What do you think would happen if we used a resistor with lower resistance? What would happen if we put two resistors in series or in parallel?

#### Part 1.B Experiment with Inverters
In this part, we will be working with PMOS and NMOS transistors. PMOS stands for P-type Metal Oxide Semiconductor. P-type semiconductors contain a larger concentration of holes as opose to electrons while N-type semiconductors are the opposite. These transistors act as switches when turn to VDD and GND. Because of this behavior, combinations of NMOS and PMOS can make many different types of logic gates. PMOS will always be connected to ground and as a switch, it is open when voltage to the gate is high and closed when voltage through the gate is low. This is opposite for NMOS where NMOS is always connected to VDD.
Wire up an inverter circuit using both a PMOS and NMOS transistor. Notice that we have already provided you with the PMOS and NMOS transistors that are wired to VDD(+) and GND(-) respectively. You will have to use a digital input switch to send a digital signal to your inverter and a digital output switch to receive the digital signal that your inverter produces. You may refer to Figures 5 and 6 below, which show both the circuit diagram for the inverter and how it should be implemented on the breadboard, respectively.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/InverterCircuit.png" width="200">
    <font size="2">
        <figcaption> Figure 5: Inverter Circuit [1] </a>
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="800">
    <font size="2">
        <figcaption> Figure 6: Breadboard Diagram for Testing Inverter Circuit </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT (CLICK ME)</I></summary>
<p>
    Looking from the flat side of the transistor with pins facing down, the left pin is the source which connects to VDD for PMOS and GND for NMOS. The right pin is the drain which connects to the output for both PMOS and NMOS. The middle pin is the gate, which connects to the input.
</p>
</details>

#### Part 1.C Developing a NAND Gate 
In this section, you will implement a more complex circuit in the NAND gate. If you still have a yellow jumper attached to both your NMOS transistors, have an instructor come over to remove one, as you’ll only need one of them to implement this gate.

Consider the circuit shown below in Figure 7. Before proceeding with your implementation, try to determine the values of the circuit for each combination of inputs(this is called a truth table). Once you have done so, implement the circuit shown on your prototyping platform and confirm that you are getting the expected results using your truth table. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/NANDGateDiagram.png" width="400">
    <font size="2">
        <figcaption> Figure 7: NAND Gate [2] </a>         
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have wired the logic gate, have an instructor verify that things are connected correctly; then the instructor will turn on the board and we can observe the functionality of the circuit. 

*Critical Thinking Questions*: Why is this gate called a NAND gate? Can we use a NAND and the inverter from the previous part to implement an AND gate? Can you think of how to implement a NOR gate?

<details><summary><I>HINT 1</I></summary>
<p>
   Sample Truth table : Fill out the output column
    
| AB        |Output          |
| ------------- |:-------------:|
| 00      |  |
| 01      |       |
| 10 |       |
| 11 |       |
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p>
   On the breadboard, observe the numbered rows and lettered columns. Connecting wires on the same rows results in parallel connections and connecting wires on the same columns results in series connections. This is true for the columns labeled "ABCDEFGHIJ". 
</p>
</details>


### Part 2. Understanding Basic Logic Gates
In the previous section, we learned about basic digital circuits and how they can be implemented. In this section, we will take what we have learned and abstract it away and eventually build a parity checker with these new gates we discovered.

#### Part 2.A Experiment with AND, OR, XOR Gates
After turning off the power supply, begin to wire up the AND gate as shown in Figure 8 below. During this process try to come up with the truth table for an AND gate, and check to see that your results are expected once you have finished up the wiring. Wire up a single gate from the other two chips in a similar fashion and come up with a truth table for each using the same process as the previous part. Using these truth tables, try to determine which gate is the XOR and which is the OR gate.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="800">
    <font size="2">
        <figcaption> Figure 8: Breadboard Diagram for Testing NAND Gate </a>
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have determined which chip contains the each type of gate, show an instructor your truth tables and demonstrate the operation of either the OR or the AND gate. 

*Critical Thinking Questions*: So far we have seen four two-input logic gates: NAND, AND, OR, and XOR. How many different logic gates are possible if we limit ourselves to gates with just two inputs and one output? 

#### Part 2.B Develop Parity Checker
In this section, you will develop a parity checker, which is useful in determining whether a message has been compromised in any way when it was being sent. A parity unit should produce a zero when there are an even number of ones in the input and a one when there are an odd number of ones in the input. This means that the total number of ones(including both the input and the parity unit) should be an even number. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/ParityChecker.png" width="600">
    <font size="2">
        <figcaption> Figure 9: Parity Checker [3] </a>
    </figcaption>
    </font>
</figure>

Figure 9 illustrates how a four-bit parity checker can be implemented using four XOR gates. Verify, by filling out the truth table below, that this is the case, and once done with the wiring, do the same with your setup, checking all combinations of inputs.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/TruthTable.png" width="200">
    <font size="2">
        <figcaption> Figure 10: Truth Table </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT 1</I></summary>
<p>
   For the truth table, there should be 16 entries since we have 4 bits and you can quickly come up with a truth table without evaulating the gates by counting the number of 1's in the input. 
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p>
   Check the documentation carefully to see which pins in the chip are the input and which pins are the output. 
</p>
</details>


### Part 3. Building a Simple Calculator
In this section, you will use all the knowledge you have previously gained about digital circuits, to work incrementally towards building a two-bit ripple-carry adder. First, you will build a half-adder, then a full adder, and then lastly combine your work with that of another group’s in order to create a two-bit ripple-carry adder.

#### Part 3.A Experiment with Half-Adder
Wire up the half-adder shown in Figure 11 below. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdder.png" width="400">
    <font size="2">
        <figcaption> Figure 11: Half-Adder </a>
    </figcaption>
    </font>
</figure>
<details><summary><I>HINT 1</I></summary>
<p>
    <I>Debugging tip</I>: Only one output light should light up when any or both switches are closed. Depending on wiring, when both switches are closed, 2nd bit light will turn on. When only one switch is closed, 1st bit light will turn on.
</p>
</details>


#### Part 3.B Develop Full Adder
Wire up the full-adder shown in Figure 12 below. This unit is complicated enough, that you should plan out your wiring ahead of time using the template in Figure 13. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/FullAdder.png" width="600">
    <font size="2">
        <figcaption> Figure 12: Full-Adder [4] </a>
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="800">
    <font size="2">
        <figcaption> Figure 13: Planning Diagram for Breadboard Implementation of Full-Adder [5] </a>
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have wired up the full-adder unit, show an instructor its operation and verify the corresponding truth table.

<details><summary><I>HINT 1</I></summary>
<p>
    <I>Debugging tip</I>: When there is only one of A, B, and Cin, S = 1, cout = 0. When two of those, S = 0, cout = 0. When all three are closed, then both S and cout = 1. 

</p>
</details>

#### Part 3.C Develop two-bit ripple-carry adder
In this last section you will combine full adders in order to develop a two-bit ripple-carry adder. Find another group that also has a completed full-adder and find a way to chain both of your integrated full-adder boards together to create a hardware unit capable of adding two two-bit numbers. The configuration is shown in Figure 14 below. Both full adders should be powered using their own batteries. Verify that this simple two-bit ripple-carry adder works.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Adder.png" width="900">
    <font size="2">
        <figcaption> Figure 14: Two-Bit Ripple-Carry Adder [6]</a>
    </figcaption>
    </font>
</figure>


Acknowledgements
---
Thanks to Professor Batten for templates on lab 1 and 2 from his CURIE Academy program. [Link](https://www.csl.cornell.edu/curie2014/)

References
---
[1] Taken From: http://slideplayer.com/slide/5067607/

[2] Taken From: https://electronics.stackexchange.com/questions/72806/preference-of-nand-nor-gates 

[3] Taken From: https://www.tutorialspoint.com/digital_circuits/digital_combinational_circuits.htm 

[4] Taken From: https://cs.stackexchange.com/questions/51255/full-adder-vs-half-adder 

[5] Taken From: https://cs.stackexchange.com/questions/51255/full-adder-vs-half-adder 


