
Lab 3: Digit Recognition
======================

In this lab assignment, you and your partner will explore the digital intelligence by implementing a simple digit recognition system using Python – an interpreted high-level programming language. Python and the machine learning algorithm called K-nearest-neighbors (KNN) will be introduced in the next section. As for the lab exercises, in part 1, you will implement and verify fundamental functions including calculating distances, sort distances, vote labels, and sort votes. Then you could move on to part 2 and build your digit recognition system locally. After achieving the error rate lower than 10%, you should upload your code to the remote server and randomly draw digits on the canvas to further test your design.

Software Description
--------------------------------

Before getting started, you should read this section carefully to learn basic knowledge about Python and KNN. In this session, the motivation for machine learning applications and the methodology of machine learning algorithm will be covered in part 1. Then part 2 will be a brief tutorial for programming in Python.

### Part 1. K-nearest neighbors
A quick question is that why should we explore machine learning applications? The answer seems obvious: we want machines to complete hard work for us. With the significant improvement of the computing ability of electronic devices, recently machine learning has become a key technique for solving problem in various areas, including image/video processing, computational biology, automotive, aerospace and manufacturing. It is a data analytics technique that teaches computers to do what comes naturally to human beings: learn from experience[1]. By leveraging machine learning algorithms to train digital systems, they can extract useful information (features) intelligently from huge amount of data, which release people from trivial tasks. One of the most popular machine learning applications is handwriting recognition.

Handwriting recognition refers to the computer’s ability to intelligently interpret handwritten inputs and is broadly applied in document processing, signature verification, and bank check clearing[3]. An important step in handwriting recognition is classification, which classifies data into one of fixed number of classes according to learning models and training sets. The typical and most popular way of classification is called supervised learning. In specific, we produce a set of already-classified data as input to a training model[4], which is a hypothesis function to approximate the corresponding problem. During the training process, the model will update the parameters; then it could make a reasonable prediction based on the pre-trained hypothesis function. 

With the name “machine learning” coined in 1969 by Arthur Samuel[5], researchers have designed various machine learning algorithms suitable for different type of problems. As one of the earliest machine learning algorithms, the KNN has a straightforward and intuitive method to classify data, that is “similar inputs have similar outputs[6]”.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" target="_blank">Link to image of blinking LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/KNNPrediction.png" width="400">
    <font size="2">
    <figcaption> Figure 1: Scheme in KNN Prediction </a> 
    </figcaption>
    </font>
</figure>

As showed in figure 1, all points are projected to a 2D hyperplane. Three of them have the label marked as “+”, and other three of them have the label marked as “-”. Then how should we  classify the new point marked as “?”? Since its nearest neighbors have 2 “+” and 1 “-”,we should label it as “+” based on the principle of “similar inputs have similar outputs”.

But what about predict digits in images? As we all know, all files are stored as numbers in electronic devices, including images. Suppose we have a colored image with a small resolution 28x28, that is we have 784 pixels in this image. Under RGB color mode, each pixel will be represented by three numbers range from 0 to 255 corresponding to Red, Green, and Blue. To simplify our design, images in the training set and the testing set are black and white picture. Figure 2 shows 2 examples in the training set.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" target="_blank">Link to image of training instance of digits</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/HandwrittenDigit.png" width="400">
    <font size="2">
    <figcaption> Figure 2: Training instance for digit 0 (a), training instance for digit 7 (b)n </a> 
    </figcaption>
    </font>
</figure>

#### Part2. Python Tutorial
In this section, you will experiment with code that will either respond to or control the LEDs, switches, and potentiometer. 	

Python, as a high-level programming language for general-purpose programming language, was the most popular programming language in 2017[9]. Most programmers start their coding journal from Python because its high code readability, clear constructs, notably syntactically significant whitespace, and abundant open-source standard libraries[10]. Moreover, it supports the dynamic automatic memory management and multiple programming paradigms including object-oriented, imperative, functional and procedural. In this part, we will go through the basic syntax and data structure using in Python.
 
There are many Python Tutorials online[11], and here we grab some basic usage for your information. Please refer to the script “example.py” to improve the understanding of Python when reading this part.

(1) The famous “Hello World” program in Python.
Print (“Hello World!”)

(2) Data type
- Int – An integer (e.g. -2, 3, 0, 2018)
- Float – A floating point number (e.g. 3.1415926, 2.718281)
- Str – A sequence of characters like texts (e.g. “Hello world!”, “3.1415926”)
- Booleans – True or False

(3) Data Structures
- List – An array of data (e.g. l = [0,1,2,3,4,5])
- Dictionary – Associative arrays (e.g. d = {‘Bob’ : 20, ‘Alice’ : 18})
- Tuple – A list of various data type (e.g. t = (‘Bob’, 20, 3.1415926))

(4) Control flow
- Conditional branch – if-elif-else
- For loop
- While loop

(5) Object-Oriented Programming (OOP)
- Function
- Class


<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" target="_blank">Link to image of blinking LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 4: Blinking LED Code Example </a> 
    </figcaption>
    </font>
</figure>

Once this is working properly, let’s try to extend the code we’ve just written such that we make one LED light up when the right bumper is pressed and the other light up when the other LED is pressed. The code for this part is shown in Figure 5 below. Verify that this works as expected after finishing and uploading the code to your Arduino.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" target="_blank">Link to image of blinking LED and switch-controlled LED code example</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/BlinkingLEDAndSwitchControlledLEDCode.png" width="400">
    <font size="2">
    <figcaption> Figure 5: Blinking LED and Switch-Controlled LED Code Example </a> 
    </figcaption>
    </font>
</figure>

Once this part is working, we can extend the code one step further, but getting the potentiometer involved as well. A potentiometer is a variable resistor, and it is located on one end of the prototyping board. Turning the blue knob will change the resistance of the potentiometer. The Arduino can read this resistance as an analog value by using an analog input pin. On our robot, the potentiometer is connected to analog input pin 5, and you will observe that analog inputs have values between 0 and 1023 when you add this extra functionality to your code. You can get the Arduino to read the potentiometer by adding this line to your loop routine:

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab2/figures/PotentiometerReadCode.png" width="400">
</figure>

After adding this statement to your code, verify that it works properly before showing your results to an instructor.

*Sign-Off Milestone*: Once you have one LED’s blink rate controlled by the potentiometer and the other LED controlled by the switch, have a teaching assistant verify that things are working correctly. 

*Critical Thinking Questions*: Explain why pressing the switch quickly sometimes does not turn on the LED, and why the LED stays lit for a short duration after you release the switch. Similarly, explain why adjusting the potentiometer sometimes requires a short duration before impacting the blink rate.

Lab Exercises
--------------------------------

In this part, you should implement four basic functions for building the digit recognition system. As for the first function, we will calculate the hamming distance of training images and the testing image. Then in the second function, we will sort the distance to find the K nearest neighbors. And we will vote for different labels (that is digits in our case) in the third function. Finally we sort the votes and return the final prediction.

For more details, please refer to the comments in the provided template called “digitrec.py”. During debugging, feel free to consulting with the TAs. 

(NEED TO ADD TIP)

*Sign-Off Milestone*: Once you have passed all the test cases provided in the test harness, show the code and results to one of the TAs before move on.

#### Part1. Experiment with Drive Motors
After passed all checking point done by the test harness, you could move to part2 – a more convincible verification of the digit recognition system. In this part, you can simply copy and paste your code implemented in part1. If the error rate is smaller than 10%, then you could move forward. 

*Sign-off Milestone*: Once you have achieved an error rate smaller then 10%, show the code and results to one of the TAs before move on.


### Part2. Robotic Behaviors
Now it’s time to deploy a web application based on your digit recognition system. Open a browser and type in the IP address “10.XX.XX.XX”. Then type in your Username and Password to login the system. After that, please double check the group number showed in the top of the website. Before starting drawing on the canvas, please upload the “digitrec.py” file created in part2 to the website. Finally you could play with your web app. Draw some weird numbers on the canvas to see whether you could fool the smart machine!

*Sign-off Milestone*: Once you have verified your web app, demonstrate the final web-based digit recognition system to one of the TAs.

#### Part3. References
[1] “What is Machine Learning? 3 things you need to know” Available at https://www.mathworks.com/discovery/machine-learning.html
[2] Kun, Jeremy. K-Nearest-Neighbors and Handwritten Digit Classi_cation. Math Programming. Available at https://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classi_cation

[3] ECE 5775 lab2 handout: Digit Recognition System (Part1). Available at http://www.csl.cornell.edu/courses/ece5775/schedule.html
[4] K-Nearest-Neighbors and Handwritten Digit Classification. Available at:
https://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classification/
[5] Machine Learning – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Machine_learning
[6] CS5780 lecture 2 handout: K-nearest-neighbors. Available at:
http://www.cs.cornell.edu/courses/cs4780/2018sp/page16/index.html
[7] Hamming distance – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Hamming_distance
[8] The MNIST Database of handwritten digits. Available at:
http://yann.lecun.com/exdb/mnist/
[9] Python Tops 2017’s Most popular Programming Languages. Available at:
https://www.extremetech.com/computing/252987-python-tops-list-2017s-popular-programming-languages
[10] Python (programming language) – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Python_(programming_language)
[11] The Python Tutorial. Available at:
https://docs.python.org/3/tutorial/index.html
