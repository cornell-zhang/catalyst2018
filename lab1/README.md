Lab 1: Mystery Circuit
======================

In this first lab assignment, both you and your partner will experiment with basic circuit components used in electronics, gradually building your way up into building a two-bit ripple-carry adder. The goal of the lab is become familiar with how circuits and digital logic work at a hardware level. In the first section, you will experiment with both basic analog and digital circuits, culminating with the creation of a logical NAND gate. In the second part, you will experiment with basic logic gates, and eventually develop a parity checker. In the last part, you will use everything you have learned thus far to incrementally build a two-bit ripple-carry adder. After finishing each section, make sure that a teaching assistant verifies the correct outcome and initials the appropriate line on the sign-off sheet. **Make sure to turn in your sign-off sheet by the end of the lab session.**


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
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/image3.jpeg" width="400">
    <font size="2">
    <figcaption> Black power cable with barrel connector </a> 
    </figcaption>
    </font>
</figure>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/image2.jpeg" width="400">
    <font size="2">
    <figcaption> The LED </a> 
    </figcaption>
    </font>
</figure>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/image1.jpeg" width="400">
    <font size="2">
    <figcaption> Resistors </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagram.png" width="800">
    <font size="2">
    <figcaption> Figure 1: Simple LED Circuit Implemented on Prototyping Platform </a> 
    </figcaption>
    </font>
</figure>



<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/supplies1.jpg" width="300">
    <font size="2">
    <figcaption> Figure 2: Supplies </a> 
    </figcaption>
    </font>
</figure>

Lab Exercises
--------------------------

### Part 1. Understanding basic circuits
In this section, you will wire up some basic circuits that start with a simple analog LED circuit and then go to other simple digital circuits before going into developing a NAND gate. We will be exploring the basic building blocks that make up all electronics. A computer contains billions of transistors. Logic gates such as the NAND gate are made up of these transistors. Inside a computer, there could be millions to billions of logic gates depending on the computer all working in conjunction to make the machine run. Understanding how these logic and basic circuit work is fundamental to understanding how a computer works. If you are ever in need of assistance, feel free to ask the TA’s for help. While you are wiring up circuits, make sure to turn OFF the breadboard power supply. Failure to do so may result in the circuit breaking. You may refer to Figure 3 below to see the wiring underlying the breadboard.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardWiring.png" width="800">
    <font size="2">
    <figcaption> Figure 3: Underlying Wiring of Breadboard </a> 
    </figcaption>
    </font>
</figure>

Looking at figure 3, let us assume the rows are denoted by the numbers, we notice that all holes in a row are connected together. This means that any circuit components with both pins connected in the same rows are in parallel to each other. Different rows are not connected. Components with only one pin connected to the same row and the other pin connected to different rows are in series with each other. Components with no pins that share a row will not affect each other. The top and bottom of the figure shows the holes connected horizontally. These holes are typically for power and ground pins from the power source and circuit components 

#### Part 1.A Experiment with LED
LED stands for Light Emitting Diodes; a diode is a semiconductor device that allows current to flow easily in one direction but restricts current flowing in opposite direction. There are many different types of diode such as Zener Diode, which allows current to flow in the opposite direction if it reaches a certain voltage. Diodes can be used to protect motors and electronics from current going in the reverse bias which can damage electronic components. The diode we are using provides light as the name suggests.
The LED must be placed in a specific direction for it to turn on. The two pins of the LED are called cathode, the short pin, and anode, the long pin. Look at the diagram in figure 4, the anode and cathode of the LED corresponds to its circuit representation. As current flows through the LED from anode to cathode, it will emmit light.   

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LED.png" width="600">
    <font size="2">
    <figcaption> Figure 4: LED Schematic </a> 
    </figcaption>
    </font>
</figure>

The circuit diagram shown in figure 5 contains three circuit components; the LED, which is the triangle with a line through it, the resistor, and the power source. The power source is denoted with a plus sign which shows the direction of current. Current always flow from higher voltage to lower voltage. Thus the current flows clockwise in figure 5. 
Wire up the simple LED circuit shown in figure 4 below. You may also refer to figure 1, which shows the circuit wired up on the breadboard. Remember to place a resistor in the circuit. The LED does not have sufficient internal resistance to prevent a short circuit. When a circuit is closed, it needs a resistor to dissipate energy, otherwise, the circuit will heat up from large amount of current going flowing through it. 
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LEDCircuitDiagram.png" width="200">
    <font size="2">
    <figcaption> Figure 5: Simple LED Circuit </a> 
    </figcaption>
    </font>
</figure>


```Sign-Off Milestone``` : Once you have wired everything up, have an instructor verify that the components are connected correctly; then the instructor will demonstrate how to plug in the barrel connector, test the circuit, and turn the board on/off using the switch on the breadboard power supply. Try putting the LED in both directions. 

*Critical Thinking Questions*: What do you think would happen if we used a resistor with higher resistance? What do you think would happen if we used a resistor with lower resistance? What would happen if we put two resistors in series or in parallel?

#### Part 1.B Experiment with Inverters
In this part, we will be working with PMOS and NMOS transistors. PMOS stands for P-type Metal Oxide Semiconductor. P-type semiconductors contain a larger concentration of holes (elements that can recieve electrons) as opose to electrons while N-type semiconductors are the opposite. These transistors are also called MOSFETs (MOS Field Effect Transistor). One defining property is that it has a "gate" that controls the current flowing through it. These transistors act as switches whose behavior is determined by input voltage when the VDD and GND are kept constant. When the input voltage exceeds a certain threshhold, the MOSFET will regulate current flow through it from acting as an open circuit or a short circuit. Thus, combinations of NMOS and PMOS can make many different types of logic gates. 

Here's a summary. Remember, PMOS and NMOS are complementary!

PMOS: 
- Closed when input is low 
- Open when input is high 
- Usually above the output in circuit diagram and connected to VDD

NMOS:
- Closed when input is high
- Open when input is low 
- Usually below the output in circuit diagram and connected to GND

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/CMOS Inverter.png" width="400">
    <font size="2">
        <figcaption> Figure 6: CMOS Inverter Circuit </a>
    </figcaption>
    </font>
</figure>

There multiple labels in the figure. The 'G' stands for Gate which is where input voltage will be applied. The gate is not directly connected to the rest of the circuit but provides a voltage difference from the gate to the circuit. This is very similar to a capacitor. In digital logic, the gate voltage is the same as input voltage. 'D' stands for Drain and 'S' stands for Source. For the MOS to change behavior, the gate voltage must be regulated such that the difference between the gate and source voltage meets some threshold. For NMOS, the gate to source voltage difference has to be greater than the threshold voltage for current to flow at all. For PMOS, the gate to source voltage difference has to be less than a threshold voltage for current to flow through it. Notice that the PMOS and NMOS have the drain connected to the output. For PMOS, current will flow from the source to drain and for the NMOS, current will flow from the drain to source. 

Wire up an inverter circuit using both a PMOS and NMOS transistor. Notice that we have already provided you with the PMOS and NMOS transistors that are wired to VDD(+) and GND(-) respectively. You will have to use a digital input switch to send a digital signal to your inverter and a digital output switch to receive the digital signal that your inverter produces. You may refer to Figure 6 above and figure 7 below, which show both the circuit diagram for the inverter and how it should be implemented on the breadboard, respectively.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagramForInverter.png" width="800">
    <font size="2">
        <figcaption> Figure 7: Breadboard Diagram For Testing Inverter Circuit </a>
    </figcaption>
    </font>
</figure>
<details><summary><I>HINT 1(CLICK ME)</I></summary>
<p>
    As seen in Figure 7, wiring is very important for debugging the circuit. A good practice is to make all the same nodes the same color. For example, make wires that have the same voltage the same color.
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p>
    Looking from the flat side of the transistor with pins facing down, the left pin is the source which connects to VDD for PMOS and GND for NMOS. The right pin is the drain which connects to the output for both PMOS and NMOS. The middle pin is the gate, which connects to the input.
</p>
</details>

#### Part 1.C Developing a NAND Gate 
In this section, you will implement a more complex circuit in the NAND gate. If you still have a yellow jumper attached to both your NMOS transistors, have an instructor come over to remove one, as you’ll only need one of them to implement this gate.

Consider the circuit shown below in figure 8. Before proceeding with your implementation, try to determine the values of the circuit for each combination of inputs(this is called a truth table). Once you have done so, implement the circuit shown on your prototyping platform and confirm that you are getting the expected results using your truth table. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/CMOS NAND.png" width="400">
    <font size="2">
        <figcaption> Figure 8: CMOS NAND Gate</a>         
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have wired the logic gate, have an instructor verify that things are connected correctly; then the instructor will turn on the board and we can observe the functionality of the circuit. 

*Critical Thinking Questions*: Why is this gate called a NAND gate? Can we use a NAND and the inverter from the previous part to implement an AND gate? Can you think of how to implement a NOR gate?

<details><summary><I>HINT 1</I></summary>
<p>
   A NAND gate is the opposite of an AND gate and outputs LOW when both inputs are HIGH and outputs HIGH otherwise. 
</p>
</details>
<details><summary><I>HINT 2</I></summary>
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
<details><summary><I>HINT 3</I></summary>
<p>
   On the breadboard, observe the numbered rows and lettered columns. Connecting wires on the same rows results in parallel connections and connecting wires on the same columns results in series connections. This is true for the columns labeled "ABCDEFGHIJ". 
</p>
</details>


### Part 2. Understanding Basic Logic Gates
In the previous section, we learned about basic digital circuits and how they can be implemented. In this section, we will take what we have learned and abstract it away and eventually build a parity checker with these new gates we discovered.

#### Part 2.A Experiment with AND, OR, XOR Gates

Figures 9 show us the circuit symbols for some basic logic gates and their accompanying truth tables. Can you write the truth table for AND? 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Logicgates.PNG" width="800">
    <font size="2">
        <figcaption> Figure 9: Circuit Symbols for Different Logic Gates [1]</a>
    </figcaption>
    </font>
</figure>

After turning off the power supply, begin to wire up the AND gate as shown in figure 10 below. During this process try to come up with the truth table for an AND gate, and check to see that your results are expected once you have finished up the wiring. Wire up a single gate from the other two chips in a similar fashion and come up with a truth table for each using the same process as the previous part. Using these truth tables, try to determine which gate is the XOR and which is the OR gate.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="800">
    <font size="2">
        <figcaption> Figure 10: Breadboard Diagram for Testing NAND Gate </a>
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have determined which chip contains the each type of gate, show an instructor your truth tables and demonstrate the operation of either the OR or the AND gate. 

*Critical Thinking Questions*: So far we have seen four two-input logic gates: NAND, AND, OR, and XOR. How many different logic gates are possible if we limit ourselves to gates with just two inputs and one output? 

#### Part 2.B Develop Parity Checker
In this section, you will develop a parity checker, which is useful in determining whether a message has been compromised in any way when it was being sent. The sender can calculate the parity of a message and send the parity bit along with the message. The receiver can then also calculate the parity of the message and compare it to the parity bit sent along with the message. If the parity bits do not match then it is likely that one of the bits in the message was corrupted. A parity unit should produce a zero when there is an even number of ones in the input and one when there is an odd number of ones in the input. This means that the total number of ones(including both the input and the parity unit) should be an even number. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/ParityChecker.png" width="600">
    <font size="2">
        <figcaption> Figure 11: Parity Checker [2] </a>
    </figcaption>
    </font>
</figure>
Figure 11 illustrates how a four-bit parity checker can be implemented using four XOR gates. Verify, by filling out the truth table below, that this is the case, and once done with the wiring, do the same with your setup, checking all combinations of inputs.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="800">
    <font size="2">
        <figcaption> Figure 12: Schematics for the three chips </a>
    </figcaption>
    </font>
</figure>

The schematics in figure 12 shows you the pin connections for the chips and what inputs and outputs each pin pretains to.  

Parity Checker Truth table : Fill out the rest
    
| W|X|Y|Z        |Output          |
| -|-|-|---------- |:-------------:|
| 0|0|0|0      |  0|
| 0|0|0 |1        |1       |
| 0|0|1 |0       | 1|
| 0|0|1 |1       |0|
| 0|1 |0 |0 |1|
| 0| | | ||
|0||||
|0||||
|1||||
|1 | | | |
|1||||
|1||||
|1||||
|1||||
|1||||
|1||||


<details><summary><I>HINT 1</I></summary>
<p>
   For the truth table, there should be 16 entries since we have 4 bits and you can quickly come up with a truth table without evaulating the gates by counting the number of 1's in the input. 
</p>
</details>


### Part 3. Building a Simple Calculator
In this section, you will use all the knowledge you have previously gained about digital circuits, to work incrementally towards building a two-bit ripple-carry adder. First, you will build a half-adder, then a full adder, and then lastly combine your work with that of another group’s in order to create a two-bit ripple-carry adder. Note the connection between the parity checker and the adder. We can first look at the XOR gates used for both devices. As we found in the previous section, the XOR gate is convenient for finding odd numbers of 1's in the input where it will output 1 for those combinations of input. This property is also useful for binary arithmetic since whenever the two inputs are 1, the addition will result in a 0 with a carry out of 1. To help understand the relationship, write the truth table for a half adder. It should have two inputs and two outputs as seen in figure 13. A carry out in binary arithmetic is similar to in decimal arithmetic where we carry over the 1..9 to the next order when the addition from the previous order is greater than 10. In binary addition, we carry over the 1 when the addition is greater than 1.   

#### Part 3.A Experiment with Half-Adder
Wire up the half-adder shown in figure 13 below. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdder.png" width="400">
    <font size="2">
        <figcaption> Figure 13: Circuit of Half-Adder </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT 1</I></summary>
<p> 
    <I>Debugging tip</I>: Only one output light should light up when any or both switches are closed. Depending on wiring, when both switches are closed, 2nd bit light will turn on. When only one switch is closed, 1st bit light will turn on.
</p>
</details>


#### Part 3.B Develop Full Adder
Wire up the full-adder shown in figure 14 below. A full adder contains a carry in which takes in the carry out from another adder. This unit is complicated enough that you should plan out your wiring ahead of time using the template in figure 15. Additionally you should extend your truth table to include a carry in. The Cin will affect the output and Cout.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Fulladder.png" width="600">
    <font size="2">
        <figcaption> Figure 14: Full-Adder </a>
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="800">
    <font size="2">
        <figcaption> Figure 15: Planning Diagram for Breadboard Implementation of Full-Adder </a>
    </figcaption>
    </font>
</figure>

```Sign-Off Milestone```: Once you have wired up the full-adder unit, show an instructor its operation and verify the corresponding truth table.
<details><summary><I>HINT 1</I></summary>
<p>
    It is very easy to complete the truth table using arithmetic rather than working through figure 14. One way to think about this is S = binary addition of A+B+Cin, while Cout = 0 if decimal addition of A+B+Cin<=1, otherwise = 1. 
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p>
    <I>Debugging tip</I>: When there is only one of A, B, and Cin, S = 1, Cout = 0. When two of those, S = 0, Cout = 0. When all three are closed, then both S and Cout = 1. 
</p>
</details>

#### Part 3.C Develop multi-bit ripple-carry adder
In this last section you will combine full adders in order to develop a two-bit ripple-carry adder. For a ripple-carry adder, the Cout of one stage acts as the Cin of the next stage. Observe figure 16, a ripple-carry adder is a combination of multiple full adders. This systems provides regularity and modularity. We can theoretically have N-bit ripple-carry adder using N adders which can handle binary addition up to N bits. The ripple-carry adder starts in the full adder for the least significant bits with carry in of zero. It first calculates the result and Cout from binary addition of the least significant bits. Then, the full adder passes the Cout to the next adder in line. The next adder takes the Cout as Cin as well as A and B to calculate its own result and Cout. It passes the Cout to the next adder in the chain until it reaches the end of the chain. The Cout for the last adder is helpful in determining if the binary addition resulted in overflow. If the Cin is not the same as the Cout, then most likely overflow occurs. The name "ripple-carry" comes from the fact that the carry moves through the system. Think about how in decimal arithmetic, we can end up carrying 1..9 multiple times if the carry results in addition greater than 10.  

Find another group that also has a completed full-adder and find a way to chain both of your integrated full-adder boards together to create a hardware unit capable of adding two two-bit numbers. The configuration is shown in figure 16 below. Both full adders should be powered using 9v batteries. You will likely need extra wires. Ask the TA's for materials and/or help. Verify that this simple two-bit ripple-carry adder works. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Adder.png" width="900">
    <font size="2">
        <figcaption> Figure 16: Multi-Bit Ripple-Carry Adder</a>
    </figcaption>
    </font>
</figure>

*Critical Thinking Questions*: What do you think is a disadvantage of the ripple-carry adder. Think about the name of the adder and what would happen if we have a large amount of full adders chained together. What would be a solution to this problem?

#### Optional Extensions
Parts 1–3 are the required portions of the lab. If you complete these parts quickly, you are free to
try one or more of the following extensions which are roughly arranged in order of difficulty. These
extensions are purely optional; do not feel like you must attempt them.
- Larger Adders – Work with other groups to build a three-bit or four-bit adder using the integrated
full-adder boards. What is the largest adder you can build? Don’t forget to work
through the expected result on paper first so you can verify that your multi-bit adder works.
- Using Your Breadboard Implementation – If you are confident that your breadboard implementation
of the full-adder module works, try connecting it to the integrated full-adder board
to create a two-bit adder.
- Larger Parity Checkers – Build a larger parity checker that can calculate the parity for an eightbit
input. You will need to use a total of seven XOR gates. Since each XOR chip only has four
XOR gates, you will need to work with another group to build this circuit.
- Implement a NOR Gate – Use PMOS and NMOS transistors to implement a NOR gate. A NOR
gate should produce a one when both inputs are zero, otherwise it should always produce a
zero.
- Subtraction Unit – We can use your ripple-carry adder to subtract two binary numbers. To
calculate A - B, we need to modify B before using the ripple-carry adder. We first invert every
bit in B (i.e., every one becomes a zero and every zero becomes a one). Then we need to add one
to the inverted version of B. If we add the result to A, it will have the same effect as subtracting B
from A. In other words, using binary arithmetic A - B = A + !B + 1, where !B means invert every
bit. You can implement the subtractor
either by working out the inversion and increment by one on paper and then using the ripplecarry
adder from Part 3. For the truly ambitious, you could implement a two-bit subtractor
by working with three other groups. Combine each groups’ breadboard implementation of
the full-adder module along with an inverter implemented using NMOS/PMOS transistors to
create the entire hardware module.
<details><summary><I>Subtractor Hint</I></summary>
<p>
    You many find this adder diagram useful
    <figure>
        <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/4thBitSubtractor.PNG" width="900">
        <font size="2">
            <figcaption> Four Bit Subtractor</a>
        </figcaption>
        </font>
    </figure>
</p>
</details>

Acknowledgements
---
Thanks to Professor Batten for templates on lab 1 and 2 from his CURIE Academy program. [Link](https://www.csl.cornell.edu/curie2014/)

References
---
[1] Taken From: David Harris, Sarah Harris, *Digital Design and Computer Architecture, 2nd edition*

[2] Taken From: https://www.tutorialspoint.com/digital_circuits/digital_combinational_circuits.htm 

[3] Taken From: https://cs.stackexchange.com/questions/51255/full-adder-vs-half-adder 



