Lab 3: Digit Recognition
======================

In this lab assignment, you and your partner will explore the digital intelligence by implementing a simple digit recognition system using Python – an interpreted high-level programming language. Python and the machine learning algorithm called K-nearest-neighbors (KNN) will be introduced in the next section. As for the lab exercises, in part 1, you will implement and verify fundamental functions including calculating distances, sort distances, vote labels, and sort votes. Then you could move on to part 2 and build your digit recognition system locally. After achieving an error rate lower than 10%, you should upload your code to the remote server and randomly draw digits on the canvas to further test your design.

Software Description
--------------------------------

Before getting started, you should read this section carefully to learn basic knowledge about Python and KNN. In this session, the motivation for machine learning applications and the methodology of machine learning algorithm will be covered in part 1. Part 2 is then brief tutorial for programming in Python.

### Part 1. K-nearest neighbors
A quick question is: why should we explore machine learning applications? The answer seems obvious: we want machines to complete hard work for us. With the significant improvement of the computing ability of electronic devices, machine learning has recently become a key technique for solving problem in various areas, including image/video processing, computational biology, automotives, aerospace and manufacturing. It is a data analytics technique that teaches computers to do what comes naturally to human beings: learn from experience[1]. By leveraging machine learning algorithms to train digital systems, they can extract useful information (features) intelligently from huge amount of data, which release people from trivial tasks. One of the most popular machine learning applications is handwriting recognition.

Handwriting recognition refers to a computer’s ability to intelligently interpret handwritten inputs and is broadly applied in document processing, signature verification, and bank check clearing[3]. An important step in handwriting recognition is classification, which classifies data into one of a fixed number of classes according to learning models and training sets. The typical and most popular type of classification is called supervised learning. Specificly, we produce a set of already-classified data as input to a training model[4], which is a hypothesis function to approximate the corresponding problem. During the training process, the model will update the parameters, allowing it to make a reasonable prediction based on the pre-trained hypothesis function. 

With the name “machine learning” coined in 1969 by Arthur Samuel[5], researchers have designed various machine learning algorithms suitable for different type of problems. As one of the earliest machine learning algorithms, the KNN has a straightforward and intuitive method to classify data: “similar inputs have similar outputs[6]”.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" target="_blank">Link to image of KNN prediction scheme</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" width="300">
    <font size="2">
    <figcaption> Figure 1: Scheme in KNN Prediction </a> 
    </figcaption>
    </font>
</figure>

As showed in figure 1, all points are projected to a 2D hyperplane. Three of them have the label marked as “+”, and other three of them have the label marked as “-”. Then how should we  classify the new point marked as “?”? Since its nearest neighbors have 2 “+” and 1 “-”,we should label it as “+” based on the principle of “similar inputs have similar outputs”.

But what about predict digits in images? As we all know, all files are stored as numbers in electronic devices, including images. Suppose we have a colored image with a small resolution 28x28, that is we have 784 pixels in this image. Under RGB color mode, each pixel will be represented by three numbers range from 0 to 255 corresponding to Red, Green, and Blue. To simplify our design, images in the training set and the testing set are black and white picture. Figure 2 shows 2 examples in the training set.

<a href="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/HandwrittenDigits.png" target="_blank">Link to image of training instance of digits</a>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/HandwrittenDigits.png" width="800">
    <font size="2">
    <figcaption> Figure 2: Training instance for digit 0 (a), training instance for digit 7 (b)n </a> 
    </figcaption>
    </font>
</figure>

### Part2. Python Tutorial
Python, as a high-level programming language for general-purpose programming language, was the most popular programming language in 2017[9]. Most programmers start their coding journal from Python because of its high code readability, clear constructs, notably syntactically significant whitespace, and abundant open-source standard libraries[10]. Moreover, it supports dynamic automatic memory management and multiple programming paradigms, including object-oriented, imperative, functional and procedural. In this part, we will go through the basic syntax and data structure of Python.
 
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

A nice 43 minutes python tutorial:
https://www.youtube.com/watch?v=N4mEzFDjqtA

Lab Exercises
--------------------------------

### Part1. Function Implementation
In this part, you should implement four basic functions for building the digit recognition system. As for the first function, we will calculate the hamming distance of training images and the testing image. The second function should then sort the distances to find its K nearest neighbors. The third function will execute a vote for different labels (that is digits in our case). Finally we sort the votes and return the final prediction. First navigate to the file,  *digitrec.py - part1*. In this file you'll see a Digit class in the beginning. Make sure to take a look at its data members and functions before going on, as you'll need to know the details of this class for the implementations that you will be doing later on. 

For more details, please refer to the comments in the provided template called “digitrec.py”. During debugging, feel free to consult with the TAs through out the course of the entire lab.

#### Part1A. Calculate Hamming Distance
First, navigate to the comment section that says, "1.calculate distance". This is where you will implement the first part of this lab assignment. In this part, you will calculate the hamming distance between the test digit(which you will notice that we have already provided to you a little further up in the code). Using the methods of the Digit class, try and calculate the hamming distance from the testing digit to each of the training images.

#### Part1B. Sort Distances
Next, navigate to the next comment section that says, "2.sort distances". In this section, we will sort the results list that we have already made in the previous part, so that we have the tuples in order of distance, from least to greatest(we would like to find the K-*nearest* neighbors, after all). To simplify this section for you, you may use one of Python's built-in functions, *sorted*, which takes the entire list of tuples, and can sort by whatever you would like to specify it to sort by. In this case, we would like to sort by distance. This will take a little bit of google-ing on your part, so make sure to ask a teaching assistant if you need any help. If you have prior coding experience, you may be interested in trying out the extension, which implements the same sorting algorithm that Python uses in its built-in function, called "Adaptive Merge Sort". Through doing this exercise, you will learn about a new programming archetype called recursion.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/TipLab3.png" width="500">
    <font size="2">
    </font>
</figure>

#### Part1C. KNN Vote
In this section, you will find the K-nearest neighbors of the testing image, and store them in a dictionary with their label as keys, and the number of digits with that label, as the value. For this reason, your loop will only iterate K times and not over the entire list. You will find the section you have to implement under, "3.knn vote". 

#### Part1D. Sort Vote
In this part, you will sort the dictionary that you just created. Feel free to search the internet on how you can sort a dictionary(make sure you know whether you want to sort the dictionary by keys or values). And as always, ask a teaching assistant if you're having trouble. When you think you have correctly implemented all four parts correctly, you may check your code using the provided tet harness. You can do so by using the terminal to run the test script. Once you have navigated to the correct directory, use *python main.py* to run the test cases. If you need any help debugging after any failed test cases, feel free to ask a teaching assistant. 

*Sign-Off Milestone*: Once you have passed all the test cases provided in the test harness, show the code and results to one of the TAs before moving on.

### Part2. Verify Digit Recognition System Locally
After passed all checking point done by the test harness, you could move to part2 – a more convincible verification of the digit recognition system. In this part, you can simply copy and paste your code implemented in part1. If the error rate is smaller than 10%, then you could move forward. 

*Sign-off Milestone*: Once you have achieved an error rate smaller then 10%, show the code and results to one of the TAs before move on.


### Part3. Deploy Digit Recognition Web Application
Now it’s time to deploy a web application based on your digit recognition system. Open a browser and type in the IP address “10.XX.XX.XX”. Then type in your Username and Password to login the system. After that, please double check that the group number shown at the top is correct. Before starting ti draw on the canvas, please upload the “digitrec.py” file created in part2 to the website. Finally, play with your web app! Draw some weird numbers on the canvas to see whether you can fool the smart machine!

*Sign-off Milestone*: Once you have verified your web app, demonstrate the final web-based digit recognition system to one of the TAs.

### Extensions
1. In this extension, we will implement a specific type of sort, called "adaptive merge sort"[12]. This is the same sort method that the built in python method, *sorted* uses when it sorts things like lists and dictionaries. Through implementing this sort method, you will learn about a programming archetype called recursion, and also a little bit about the through process that goes behind making an algorithm like this one. To make this function, you will need to make three separate functions, all of which have comment blocks over them. The first funciton will be the "main" function that will use recursion. In this function, you will have, first a base case, when the size of the list is small enough that you know the answer right off the bat. In this case, a list with only one element will always be sorted. Then, you will move onto the recursive case. First, you will partition the array into two halves. The first sub-array will contain all even-indexed elements in the array, while the second sub-array will contain all odd-indexed elements. If we happen to be lucky and the two of these array happen to be sorted right off the bat, we can proceed to merge the sorted arrays together(our second function will check whether these two sub-arrays are sorted, and our third function will merge two sorted arrays together, into one sorted array). In the rest of our "main" function, we either return the sorted array after merging, if we got "lucky". In the case that we didn't, however, we will recurse on the two halves that we made, and sort in the same way. Notice that this recursion will terminate due to the base case. If we didn't have the base case there, we would get an 'indexOutOfBounds' error, which would mean that we tried to access a list element that's not actually in the list(one that's either before the first element, or past the last element). To prevent this from happening, we must have a base case. Always make sure that when you're doing recursion, that you're making the problem progressively smaller as well.

### References
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

[12] Adaptive Merge Sort. Available at:
https://www.cs.waikato.ac.nz/~tcs/COMP317/adaptivesort.html
