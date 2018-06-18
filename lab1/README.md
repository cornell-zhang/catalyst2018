Lab 1: Mystery Circuit
======================

In this first lab assignment, both you and your partner will experiment with basic circuit components, gradually building your way up into building a two-bit ripple-carry adder. In the first section, you will experiment with both basic analog and digital circuits, culminating with the creation of a NAND gate. In the second part, you will experiment with basic logic gates, and eventually develop a parity checker. In the last part, you will use everything you have learned thus far to incrementally build a two-bit ripple-carry adder. After finishing each section, make sure that a teaching assistant verifies the correct the correct outcome and initials the appropriate line on the sign-off sheet. **Make sure to turn in your sign-off sheet by the end of the lab session.**


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

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagram.png" target="_blank">Link to image of prototyping platform</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardDiagram.png" width="400">
    <font size="2">
    <figcaption> Figure 1: Simple LED Circuit Implemented on Prototyping Platform </a> 
    </figcaption>
    </font>
</figure>





<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/supplies1.jpg" target="_blank">Link to image of supplies</a>

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
In this section, you will wire up some basic circuits that start with a simple analog LED circuit and then go to other simple digital circuits before going into developing a NAND gate. If you are ever in need of assistance, feel free to ask the TA’s for help. While you are wiring up circuits, make sure to turn OFF the breadboard power supply. Failure to do so may result in the circuit breaking. You may refer to Figure 3 below to see the wiring underlying the breadboard.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardWiring.png" target="_blank">Link to image of breadboard wiring</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/BreadboardWiring.png" width="400">
    <font size="2">
    <figcaption> Figure 3: Underlying Wiring of Breadboard </a> 
    </figcaption>
    </font>
</figure>

#### Part1.A Experiment with LED
Wire up the simple LED circuit shown in Figure 4 below. You may also refer to Figure 1 since it shows the circuit wired up on the breadboard.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LEDCircuitDiagram.png" target="_blank">Link to image of LED circuit</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/LEDCircuitDiagram.png" width="200">
    <font size="2">
    <figcaption> Figure 4: Simple LED Circuit </a> 
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have wired everything up, have an instructor verify that the components are connected correctly; then the instructor will demonstrate how to plug in the barrel connector, test the circuit, and turn the board on/off using the switch on the breadboard power supply. Try putting the LED in both directions. 

*Critical Thinking Questions*: What do you think would happen if we used a resistor with higher resistance? This would be equivalent to using an even narrower pipe in our water circuit analogy. What do you think would happen if we used a resistor with lower resistance? What would happen if we put two resistors in series or in parallel?

#### Part1.B Experiment with Inverters
Wire up an inverter circuit using both a PMOS and NMOS transistor. Notice that we have already provided you with the PMOS and NMOS transistors that are wired up to VDD(+) and GND(-) respectively. You will have to use a digital input switch to send a digital signal to your inverter and a digital output switch to receive the digital signal that your inverter produces. You may refer Figures 5 and 6 below, which show both the circuit diagram for the inverter and how it should be implemented on the breadboard, respectively.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/InverterCircuit.png" target="_blank">Link to image of inverter circuit</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/InverterCircuit.png" width="200">
    <font size="2">
    <figcaption> Figure 5: Inverter Circuit </a>
        Taken From: http://slideplayer.com/slide/5067607/ </a>
    </figcaption>
    </font>
</figure>

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" target="_blank">Link to image of breadboard diagram for testing inverter circuit</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="400">
    <font size="2">
        <figcaption> Figure 6: Breadboard Diagram for Testing Inverter Circuit </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT (CLICK ME)</I></summary>
<p>
    Looking from the flat side of the transistor with pins facing down, left pin is the source which connects to VDD for PMOS and GND for NMOS. Right pin is the drain which connect to the output for both PMOS and NMOS. The middle pin is the gate for both which connects to the input.
</p>
</details>

#### Part1.C Developing a NAND Gate 
In this section, you will implement a more complex circuit in the NAND gate. If you still have a yellow jumper attached to both your NMOS transistors, have an instructor come over to remove one, as you’ll only need one of them to implement this gate.

Consider the circuit shown below in Figure 7. Before proceeding with your implementation, try to determine the values of the circuit for each combination of inputs(this is called a truth table). Once you have done so, implement the circuit shown on your prototyping platform and confirm that you are getting the expected results using your truth table. 

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/NANDGateDiagram.png" target="_blank">Link to image of NAND Gate</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/NANDGateDiagram.png" width="400">
    <font size="2">
        <figcaption> Figure 7: NAND Gate </a>
            Taken From: https://electronics.stackexchange.com/questions/72806/preference-of-nand-nor-gates </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have wired the logic gate, have an instructor verify that things are connected correctly; then the instructor will turn on the board and we can observe the functionality of the circuit. 

*Critical Thinking Questions*: Why is this gate called a NAND gate? Can we use a NAND and the inverter from the previous part to implement an AND gate? Can you think of how to implement a NOR gate?

<details><summary><I>HINT 1</I></summary>
<p>
   Sample Truth table
    
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

#### Part2.A Experiment with AND, OR, XOR Gates
After turning off the power supply, begin to wire up the AND gate as shown in Figure 8 below. During this process try to come up with the truth table for an AND gate, and check to see that your results are expected once you have finished up the wiring. Wire up a single gate from the other two chips in a similar fashion and come up with a truth table for each using the same process as the previous part. Using these truth tables, try to determine which gate is the XOR and which is the OR gate.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" target="_blank">Link to image of breadboard diagram for testing NAND gate</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/IntegratedCircuitDiagram.png" width="400">
    <font size="2">
        <figcaption> Figure 8: Breadboard Diagram for Testing NAND Gate </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have determined which chip contains the each type of gate, show an instructor your truth tables and demonstrate the operation of either the OR or the AND gate. 

*Critical Thinking Questions*: So far we have see four two-input logic gates: NAND, AND, OR, and XOR. How many different logic gates are possible if we limit ourselves to gates with just two inputs and one output? 

#### Part2.B Develop Parity Checker
In this section, you will develop a parity checker, which is useful in determining whether a message has been compromised in any way when it was being sent. A parity unit should produce a zero when there are an even number of ones in the input and a one when there are an odd number of ones in the input. This means that the total number of ones(including both the input and the parity unit) should be an even number. 

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/ParityChecker.png" target="_blank">Link to image of parity checker</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/ParityChecker.png" width="300">
    <font size="2">
        <figcaption> Figure 9: Parity Checker </a>
        Taken From: https://www.tutorialspoint.com/digital_circuits/digital_combinational_circuits.htm </a>
    </figcaption>
    </font>
</figure>

Figure 9 illustrates how a four-bit parity checker can be implemented using four XOR gates. Verify, by filling out the truth table below, that this is the case, and once done with the wiring, do the same with your setup, checking all combinations of inputs.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/TruthTable.png" target="_blank">Link to image of truth table</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/TruthTable.png" width="200">
    <font size="2">
        <figcaption> Figure 10: Truth Table </a>
    </figcaption>
    </font>
</figure>

<details><summary><I>HINT 1</I></summary>
<p>
   For the truth table, there should be 16 entries since we have 4 bits and  You can quickly come up with a truth table without evaulating the gates by counting the number 1's in the input. 
</p>
</details>


### Part 3. Building a Simple Calculator
In this section, you will use all the knowledge you have previously gained about digital circuits, to work incrementally towards building a two-bit ripple-carry adder. First, you will build a half-adder, then a full adder, and then lastly combine your work with that of another group’s in order to create a two-bit ripple-carry adder.

#### Part3.A Experiment with Half-Adder
Wire up the half-adder shown in Figure 11 below. 

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdder.png" target="_blank">Link to image of half-adder</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/HalfAdder.png" width="200">
    <font size="2">
        <figcaption> Figure 11: Half-Adder </a>
    </figcaption>
    </font>
</figure>

#### Part3.B Develop Full Adder
Wire up the full-adder shown in Figure 12 below. This unit is complicated enough, that you should plan out your wiring ahead of time using the template in Figure 13. 

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/FullAdder.png" target="_blank">Link to image of full-adder</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/FullAdder.png" width="300">
    <font size="2">
        <figcaption> Figure 12: Full-Adder </a>
        Taken From: https://cs.stackexchange.com/questions/51255/full-adder-vs-half-adder </a>
    </figcaption>
    </font>
</figure>

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" target="_blank">Link to image of full-adder</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/PlanningDiagramFullAdder.png" width="400">
    <font size="2">
        <figcaption> Figure 13: Planning Diagram for Breadboard Implementation of Full-Adder </a>
        Taken From: https://cs.stackexchange.com/questions/51255/full-adder-vs-half-adder </a>
    </figcaption>
    </font>
</figure>

*Sign-Off Milestone*: Once you have wired up the full-adder unit, show an instructor its operation and verify the corresponding truth table.

#### Part3.C Develop two-bit ripple-carry adder
In this last section you will combine full adders in order to develop a two-bit ripple-carry adder. Instead of using more logic gates, however, we will abstract away the logic behind the implementation of a full adder, by using a full-adder board, which is basically a printed circuit board that has the same circuit that you just built. You will see that it has three input switches corresponding to the three one-bit inputs. It also includes a “mode switch” which can be set to either “independent mode” or “chain mode”. Set the integrated full-adder board to “independent mode” and test its operation. Power the integrated full-adder board using a 9 V battery. Verify that it produces the same truth table as the full-adder you implemented in the previous subpart. 

Now find another lab group that is at the same step. Chain both of your integrated full-adder boards together to create a hardware unit capable of adding two two-bit numbers. The configuration is shown in Figure 14 below. Both full adders should be powered using their own batteries. The integrated full-adder board on the right should be set to “independent mode” and the integrated full-adder board on the left should be set to “chain mode”. Verify that this simple two-bit ripple-carry adder works.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/TwoBitRippleCarryAdder.png" target="_blank">Link to image of two-bit ripple-carry adder</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab1/figures/TwoBitRippleCarryAdder.png" width="300">
    <font size="2">
        <figcaption> Figure 14: Two-Bit Ripple-Carry Adder </a>
        Taken From: https://cse.buffalo.edu/~sheenara/LabAssignment.html </a>
    </figcaption>
    </font>
</figure>
