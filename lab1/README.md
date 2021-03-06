Lab 1: Digital Calculator
======================

In this first lab assignment, both you and your partner will experiment with basic circuit components used in electronics, gradually building your way up into building a two-bit ripple-carry adder. The goal of the lab is become familiar with how circuits and digital logic work at a hardware level. In the first section, you will experiment with both basic analog and digital circuits. In the second part, you will experiment with basic logic gates, and eventually develop a parity checker. In the last part, you will use everything you have learned thus far to incrementally build a two-bit ripple-carry adder. After finishing each section, make sure that a teaching assistant verifies the correct outcome and initials the appropriate line on the sign-off sheet. **Make sure to turn in your sign-off sheet by the end of the lab session.**


Hardware Description
--------------------------------

Notice that we have given you not just a breadboard, but also some components that have already been wired up. You can verify that you aren’t missing any components on the breadboard by looking at Figure 1 below. You will also be able to use any of the supplies shown below in Figure 2. You should try to identify:
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
    <figcaption> Black power cable with barrel connector<br> </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/image2.jpeg" width="400">
    <font size="2">
    <figcaption> The LED<br> </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/image1.jpeg" width="400">
    <font size="2">
    <figcaption> Resistors<br> </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagram.png" width="800">
    <font size="2">
    <figcaption> Figure 1: Simple LED Circuit Implemented on Prototyping Platform<br> </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/supplies1.jpg" width="300">
    <font size="2">
    <figcaption> Figure 2: Supplies<br> </a> 
    </figcaption>
    </font>
</figure>

Lab Exercises
--------------------------

### Part 1. Understanding basic circuits
In this section, you will wire up some basic circuits that start with a simple analog LED circuit and understand basic logic gates. A computer contains billions of transistors. Logic gates such as the AND gate are made up of these transistors. Inside a computer, there could be millions to billions of logic gates depending on the computer all working in conjunction to make the machine run. Understanding how these logic gates and basic circuits work is fundamental to understanding how a computer works. If you are ever in need of assistance, feel free to ask the TA’s for help. While you are wiring up circuits, make sure to turn OFF the breadboard power supply. Failure to do so may result in the circuit breaking. You may refer to Figure 3 below to see the wiring underlying the breadboard.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardWiring.png" width="800">
    <font size="2">
    <figcaption> Figure 3: Underlying Wiring of Breadboard <br></br></a> 
    </figcaption>
    </font>
</figure>

Looking at figure 3, let us assume the rows are denoted by the numbers (they are really faded in the figure), we notice that all holes in a row are connected. This means that any circuit components with both pins connected to the same rows are in parallel to each other. For example, if we connect one pin of resistor (R1) to row 1 and its other pin to row 2 and we do the same with another resistor (R2), then the two resistors are in parallel with each other and the equivalent resistance will be ```(R1*R2)/(R1+R2)```. Alternatively, if we connect one resistor (R3) to row 2 and row 3, then R3 will be in series with R1 and R2 and the equivalent resistance will be ```(R1*R2)/(R1+R2)+R3```. Remember to never connect the pins of your circuit component to the same row. The component will not work. The top and bottom of the figure shows the holes connected horizontally. These holes are typically for power and ground pins from the power source and circuit components. 

<details><summary><I>Circuit Example (Click me)</I></summary>
<p>
	<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/circuitexample.png" width="600">
    <font size="2">
    <figcaption> <br></br> Circuit example. If we want to connect that circuit to the breadboard, we would connect one pin of R1 to the (+) of the battery and another pin to row 1. Then we would connect one pin of R2 to row 1 and another to row 2. For the parallel configuration of R3 and R4, we will first connect one pin of each R3 and R4 to row 2 to establish a series connection. Then we will connect the second pin of both R3 and R4 to the the (-) of the battery, otherwise known as ground (GND).<br></br></a> 
    </figcaption>
    </font>
</figure>
</p>
</details>


#### Part 1.A Experiment with LED
LED stands for Light Emitting Diodes; a diode is a semiconductor device that allows current to flow easily in one direction but restricts current flowing in opposite direction. LED's are especially useful for its low energy consumption and smaller size, which makes it possible to use for our lab! 
The LED must be placed in a specific direction for it to turn on. The two pins of the LED are called cathode, the short pin, and anode, the long pin. Look at the diagram in Figure 4, the anode and cathode of the LED corresponds to its circuit representation. As current flows through the LED from anode to cathode, it will emit light.   

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LED.png" width="600">
    <font size="2">
    <figcaption> Figure 4: LED Schematic<br></a> 
    </figcaption>
    </font>
</figure>

*Circuit Intuition:*
We will quickly go over some basic electrical terms such as current and voltage

The circuit diagram shown in Figure 5 contains three circuit components; the LED, the resistor, and the power source. The power source, which can be a battery or a plug, is denoted with a plus sign which shows the location of higher voltage. Voltage is the difference between two electrical potentials. Electrical potential is a measure of the potential to do work for electrical components. This is similar to gravitational potential energy in mechanics. Just like its mechanics counterpart, voltage is relative. Current always flow from higher voltage to lower voltage. Thus, the current flows clockwise in Figure 5. A resistor in an electrical circuit is analogous to a narrow segment of pipe in a water circuit; both the resistor and the narrow pipe serve to restrict the flow of current. So, the greater the resistance (narrower the pipe) the less current can flow through circuit.

Wire up the simple LED circuit shown in Figure 5 below. You may also refer to Figure 1, which shows the circuit wired up on the breadboard. **Remember to place a resistor in the circuit.** The LED does not have sufficient internal resistance to prevent a short circuit, a low resistance connection that can result in the power source being destroyed. When a circuit is closed, it needs a resistor to dissipate energy, otherwise, the circuit will heat up from large amount of current going flowing through it. 
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LEDCircuitDiagram.png" width="200">
    <font size="2">
    <figcaption> Figure 5: Simple LED Circuit<br></a> 
    </figcaption>
    </font>
</figure>


```diff
-Sign-Off Milestone-
```

Once you have wired everything up, have an instructor verify that the components are connected correctly; then the instructor will demonstrate how to plug in the barrel connector, test the circuit, and turn the board on/off using the switch on the breadboard power supply. Try putting the LED in both directions. 

*Critical Thinking Questions*: What do you think would happen if we used a resistor with higher resistance? What do you think would happen if we used a resistor with lower resistance? What would happen if we put two resistors in series or in parallel?

#### Part 1.B Experiment with Inverters
In this part, we will be working with PMOS and NMOS transistors. PMOS stands for P-type Metal Oxide Semiconductor. P-type semiconductors contain a larger concentration of holes (elements that can receive electrons) as opposed to electrons while N-type semiconductors are the opposite. These transistors are also called MOSFETs (MOS Field Effect Transistor). One defining property of a transistor is that it has a "gate" that controls the current flowing through it. When this gate is closed, it closes the circuit and allows current to flow. When the gate is open, the circuit is open and all current is stopped. These transistors act as switches whose behavior is determined by input voltage to the gate. When the input voltage exceeds a certain threshold, the MOSFET will regulate current flow through it from acting as an open circuit or a closed circuit. Thus, combinations of NMOS and PMOS can make several types of logic gates. 

Here's a summary. Remember, PMOS and NMOS are complementary and are often used together in circuits as in figure 6!

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
        <figcaption> Figure 6: CMOS (Complementary MOS) Inverter Circuit <br></br> </a>
    </figcaption>
    </font>
</figure>

There multiple labels in the figure. The 'G' stands for Gate which is where input voltage will be applied. The gate is not directly connected to the rest of the circuit but provides a voltage difference from the gate to the circuit. In digital logic, the gate voltage is the same as input voltage. 'D' stands for Drain and 'S' stands for Source. For the MOS to change behavior, the gate voltage must be regulated such that the difference between the gate and source voltage meets some threshold. For NMOS, the gate to source voltage difference must greater than the threshold voltage for current to flow at all. For PMOS, the gate to source voltage difference must less than a threshold voltage for current to flow through it. Notice that the PMOS and NMOS have the drain connected to the output. For PMOS, current will flow from the source to drain and for the NMOS, current will flow from the drain to source.

Wire up an inverter circuit using both a PMOS and NMOS transistor. An inverter inverts the input signal. A high signal becomes low while a low signal becomes high. This is also known as a NOT gate where the output is the opposite of the input as seen in Figure 7. The bar above the A means that we are inverting the value of A. In Figure 7, the bubble or circle at the tip of the triangle facing Y is the symbol for NOT. We will be observing other logic gates later in the session; some gates will have circles attached to the input or output terminals. These suggests that we are inverting the terminal. Before proceeding with your implementation, try to determine the output of the circuit for each possible input (this is called a truth table).

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Notgate.PNG" width="200">
    <font size="2">
        <figcaption> Figure 7: NOT gate <br></br></a>
    </figcaption>
    </font>
</figure>

Notice that we have already provided you with the PMOS and NMOS transistors that are wired to VDD (+) and GND (-) respectively. You will have to use a digital input switch to send a digital signal to your inverter and a digital output switch to receive the digital signal that your inverter produces. You may refer to Figure 6 above and Figure 8 below, which show both the circuit diagram for the inverter and how it should be implemented on the breadboard, respectively.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagramForInverter.png" width="800">
    <font size="2">
        <figcaption> Figure 8: Breadboard Diagram For Testing Inverter Circuit <br></a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT 1(CLICK ME)</I></summary>
<p>
	NOT Gate with Truth Table
	<figure>
		<img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Notgate_sol.png" width="200">
	</figure>
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p>
    As seen in Figure 8, wiring is very important for debugging the circuit. A good practice is to make all the same nodes the same color. For example, make wires that have the same voltage the same color.
</p>
</details>
<details><summary><I>HINT 3</I></summary>
<p>
    Looking from the flat side of the transistor with pins facing down, the left pin is the source which connects to VDD for PMOS and GND for NMOS. The right pin is the drain which connects to the output for both PMOS and NMOS. The middle pin is the gate, which connects to the input.
</p>
</details>

### Part 2. Understanding Basic Logic Gates
In the previous section, we learned about basic digital circuits and how they can be implemented. In this section, we will take what we have learned and abstract it away and eventually build a parity checker with these new gates we discovered.

#### Part 2.A Experiment with AND, OR, XOR Gates

Figures 9 show us the circuit symbols for some basic logic gates and their accompanying truth tables.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Logicgates2.png" width="500">
    <font size="2">
        <figcaption> Figure 9: Circuit Symbols for Different Logic Gates [1] <br></br></a>
    </figcaption>
    </font>
</figure>

After turning off the power supply, begin to wire up the AND gate as shown in Figure 10 below. You should check that the behavior of the chip matches the AND truth table in Figure 9. After you confirm the behavior of this chip, wire up the other two chips in a similar fashion and come up with a truth table for each. Using these truth tables, try to determine which gate is the XOR and which is the OR gate.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="800">
    <font size="2">
        <figcaption> Figure 10: Breadboard Diagram for Testing AND Gate <br></br></a>
    </figcaption>
    </font>
</figure>


```diff
-Sign-Off Milestone-
```

 Once you have determined which chip contains each type of gate, show an instructor your truth tables and demonstrate the operation of either the OR or the XOR gate. 

*Critical Thinking Questions*: So far, we have seen four two-input logic gates: AND, OR, and XOR. How many different logic gates are possible if we limit ourselves to gates with just two inputs and one output? 

#### Part 2.B Develop Parity Checker
In this section, you will develop a parity checker, which is often used to check for errors in digital transmissions. Digital messages are always binary (it is the language of computers!) and are composed entirely of ones and zeros. The parity checker takes advantage of this fact by counting the number of ones and zeros to check for errors in the message.  Parity checker can be even or odd parity. An even parity unit produces a zero when there is an even number of ones in the input and one when there is an odd number of ones in the input, which signifies that there is an error in the input. This means that the total number of ones (including both the input and the parity unit) should be an even number. The sender can calculate the parity of a message and send the parity bit along with the message. The receiver can then also calculate the parity of the message and compare it to the parity bit sent along with the message. If the parity bits do not match, then it is likely that one of the bits in the message was corrupted. We will be implementing an even parity checker.

Figure 11 illustrates how a four-bit parity checker can be implemented using three XOR gates. Fill out the truth table below and build the parity checker using Figure 11. After you are done, make sure the truth table you fill out and the circuit you built agree by checking different combinations of inputs.

Parity Checker Truth table: Fill out the rest
    
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


<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/ParityChecker.png" width="600">
    <font size="2">
        <figcaption> Figure 11: Parity Checker [2] <br></br> </a>
    </figcaption>
    </font>
</figure>

The schematics in Figure 12 shows you the internal connections for the chips and pin connections on breadboard. Notice that each chip contains multiple gates of the same type. Each chip requires a power (VDD) and a common ground (GND). 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="800">
    <font size="2">
        <figcaption> Figure 12: Schematics for the three chips <br></br></a>
    </figcaption>
    </font>
</figure>


<details><summary><I>HINT 1</I></summary>
<p>
   For the truth table, there should be 16 entries since we have 4 bits and you can quickly come up with a truth table without evaulating the gates by counting the number of 1's in the input. 
</p>
</details>


### Part 3. Building a Simple Calculator
In this section, you will use all the knowledge you have previously gained about digital circuits to work incrementally towards building a two-bit ripple-carry adder. First, you will build a half-adder, then a full adder, and then lastly combine your work with that of another group’s to create a two-bit ripple-carry adder. 

*Binary Arithmetic*
We will be building a calculator that uses binary addition to calculate the addition of two numbers. Computers use
digital circuits which can only handle logic ones and zeros; in other words, computers work with binary numbers (i.e., base 2) and binary arithmetic. This contrasts with how we usually use decimal numbers (i.e., base 10) and decimal arithmetic. Let’s quickly review decimal numbers: each digit can be a number between zero and nine. The first digit is the “one's digit” (10<sup>0</sup>), the second digit is the “tens digit” (10<sup>1</sup>), the third digit is the “hundreds digit” (10<sup>2</sup>), and so on. We multiply the number in each digit by 10<sup>i</sup> where i indicates which digit. For binary numbers: each digit can only be zero or one. The first digit is the “one's digit” (2<sup>0</sup>), the second digit is the “twos digit” (2<sup>1</sup>), the third digit is the “fours digit” (2<sup>2</sup>), and so on. We multiply the number in each digit by 2<sup>i</sup> where i indicates which digit. Binary addition works exactly like decimal addition, where we add the "ones" digits together, "twos" digit together, and so on.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/decimalRep.png" width="800">
    <font size="2">
        <figcaption> Figure 13: Binary and Decimal Representation <br></br></a>
    </figcaption>
    </font>
</figure>
<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/stepsForbinadd.png" width="350">
    <font size="2">
        <figcaption> Figure 14: Example using binary addition for 3 + 6. 
		In the first step, we add the “one's digit”; one plus zero is one. In the second step, we add the “twos digit”; one plus one is two but remember we cannot use two in binary numbers. We can only use zero or one. We need to carry a one to the next digit. This is the same as carrying a one when performing decimal arithmetic. In the third step, we add one (the carry bit) plus zero plus one to again get two, so we again must carry a one to the next digit. In the last step, we simply add one plus zero plus zero to get the final answer: 1001 which is nine in decimal. As expected three plus six is nine, but we have now demonstrated how to do this addition using binary arithmetic.</a>
    </figcaption>
    </font>
</figure>


#### Part 3.A Experiment with Half-Adder
A half-adder can add two one-bit numbers together. As in binary arithmetic, answers greater than one is carried over to the next bit which is also known as the carry out.

Thus, how do we "add" two numbers together using logic gates? As we found in the previous section, the XOR gate is convenient for finding odd numbers of 1's in the input where it will output 1 for those combinations of input. This property is also useful for binary arithmetic since whenever the two inputs are 1, the addition will result in a 0 with a carry out of 1. To help understand the relationship, write the truth table for the half adder. It should have two inputs and two outputs as seen in Figure 13. 

Wire up the half-adder shown in Figure 13 below. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdder.png" width="400">
    <font size="2">
        <figcaption> Figure 13: Circuit of Half-Adder<br> </a>
    </figcaption>
    </font>
</figure>
<details><summary><I>HINT 1</I></summary>
<p> 
	Half-Adder with Truth table
    <figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdderTruthtable.png" width="300">
	</figure>
</p>
</details>
<details><summary><I>HINT 2</I></summary>
<p> 
    <I>Debugging tip</I>: Only one output light should light up when any or both switches are closed. Depending on wiring, when both switches are closed, 2nd bit light will turn on. When only one switch is closed, 1st bit light will turn on.
</p>
</details>


#### Part 3.B Develop Full Adder
Wire up the full-adder shown in Figure 14 below. A full adder contains a carry in which takes in the carry out from another adder. This unit is complicated enough that you should plan out your wiring ahead of time using the template in Figure 15. Additionally, you should extend your truth table to include a carry in. The Cin will affect the output and Cout.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Fulladder.png" width="600">
    <font size="2">
        <figcaption> Figure 14: Full-Adder <br></a>
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="800">
    <font size="2">
        <figcaption> Figure 15: Planning Diagram for Breadboard Implementation of Full-Adder<br></a>
    </figcaption>
    </font>
</figure>


```diff
-Sign-Off Milestone-
```

 Once you have wired up the full-adder unit, show an instructor its operation and verify the corresponding truth table.

<details><summary><I>HINT 1</I></summary>
<p>
    It is very easy to complete the truth table using arithmetic rather than working through Figure 14. One way to think about this is S = binary addition of A+B+Cin, while Cout = 0 if decimal addition of A+B+Cin<=1, otherwise = 1. 
</p>
</details>

<details><summary><I>HINT 2</I></summary>
<p>
	Full-Adder with Truth table
    <figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/FullAdderTruthtable.png" width="300">
	</figure> 
</p>
</details>
<details><summary><I>HINT 3</I></summary>
<p>
    <I>Debugging tip</I>: When there is only one of A, B, and Cin, S = 1, Cout = 0. When two of those, S = 0, Cout = 0. When all three are closed, then both S and Cout = 1. 
</p>
</details>

#### Part 3.C Develop multi-bit ripple-carry adder
In this last section you will combine full adders in order to develop a two-bit ripple-carry adder. For a ripple-carry adder, the Cout of one stage acts as the Cin of the next stage. Observe Figure 16, a ripple-carry adder is a combination of multiple full adders. This system provides regularity and modularity. We can theoretically have N-bit ripple-carry adder using N adders which can handle binary addition up to N bits. The ripple-carry adder starts in the full adder for the least significant bits (the "ones" digit) with carry in of zero. It first calculates the result and Cout from binary addition of the least significant bits. Then, the full adder passes the Cout to the next adder in line. The next adder takes the Cout as Cin as well as A and B to calculate its own result and Cout. It passes the Cout to the next adder in the chain until it reaches the end of the chain. The Cout for the last adder is helpful in determining if the binary addition resulted in overflow. If the Cin is not the same as the Cout, then most likely overflow occurs. The name "ripple-carry" comes from the fact that the carry moves through the system. Think about how in decimal arithmetic, we can end up carrying 1..9 multiple times if the carry results in addition greater than 10 for the digits of the next order.  

Figure 16 shows how we can chain a bunch of full adders to create a N-bit ripple carry adder.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/Adder.png" width="900">
    <font size="2">
        <figcaption> Figure 16: Multi-Bit Ripple-Carry Adder<br></a>
    </figcaption>
    </font>
</figure>


```diff
-Sign-Off Milestone-
```
 
Find another group that also has a completed full-adder and find a way to chain both of your integrated full-adder boards together to create a hardware unit capable of adding two two-bit numbers. The configuration is shown in Figure 16 below. Both full adders should be powered using 9v batteries. You will likely need extra wires. Ask the TA's for materials and/or help. Verify that this simple two-bit ripple-carry adder works. 

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
- Larger Parity Checkers – Build a larger parity checker that can calculate the parity for an eight-bit
input. You will need to use a total of seven XOR gates. Since each XOR chip only has four
XOR gates, you will need to work with another group to build this circuit.
- Implement a NOR Gate – Use PMOS and NMOS transistors to implement a NOR gate. A NOR
gate should produce a one when both inputs are zero, otherwise it should always produce a
zero.
- Subtraction Unit – We can use your ripple-carry adder to subtract two binary numbers. To
calculate A - B, we need to modify B before using the ripple-carry adder. We first invert every
bit in B (i.e., everyone becomes a zero and every zero becomes a one). Then we need to add one
to the inverted version of B. If we add the result to A, it will have the same effect as subtracting B
from A. In other words, using binary arithmetic A - B = A + !B + 1, where !B means invert every
bit. You can implement the subtractor
either by working out the inversion and increment by one on paper and then using the ripple-carry
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
            <figcaption> Four Bit Subtractor<br></a>
        </figcaption>
        </font>
    </figure>
</p>
</details>

Acknowledgements
---
This lab handout is derived from the 2014 CURIE Academy "[Computer Engineering -- Hardware Perspective](https://www.csl.cornell.edu/curie2014/lab1.html)" lab designed by Professor Christopher Batten.

References
---
[1] Taken From: David Harris, Sarah Harris, *Digital Design and Computer Architecture, 2nd edition*

[2] Taken From: https://www.tutorialspoint.com/digital_circuits/digital_combinational_circuits.htm 



