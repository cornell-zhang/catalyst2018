Lab 3: Handwritten Digit Recognition
======================
Why should we explore machine learning applications? The answer seems obvious: we want machines to complete hard work for us. With the significant improvement of the computing ability of electronic devices, machine learning has recently become a key technique for solving problems in various areas, including image/video processing, computational biology, the automotive industry, aerospace engineering, and manufacturing. It is a data analytics technique that teaches computers to do what comes naturally to human beings: learn from experience[1]. By leveraging machine learning algorithms to train digital systems, they can extract useful information (features) intelligently from huge amounts of data, which release people from trivial tasks. One of the most well-known machine learning applications is handwriting recognition.

In the last lab, you build a smart robot who can randomly serach and find a target. Now let's make it even more smart by building a brain for it! In this lab assignment, you and your partner will explore digital intelligence by implementing a simple digit recognition system using Python – an interpreted high-level programming language and the algorithem is called K-nearst-neighbors (KNN), which will be introduced in the next section - Turtorials. The first part describes the algorithm for digit recognition system, that is K-nearst-neighbors (KNN). Then the second part introduces the Google Colab - an online Google-drive based Python IDE. The final part is a Colab based Python notebook, which covers basic usage and detailed explanation of Python. If you were new to Python, please spend enough time on it. As for the lab exercises, the first three sections in the first part requires you implement and verify fundamental functions includes calculating distances, sorting distances, and vote for the final result/prediction. Then, you can move to the last section of Part 1 and build your digit recognition system. After achieving an error rate lower than 10%, you could move to Part 2: upload your code to the remote server and randomly draw digits on the canvas to further test your design.

Tutorials
--------------------------------

Before getting started, you should read this section carefully to learn basic knowledge about Python and KNN. In this section, the motivation for machine learning applications and the methodology of machine learning algorithms will be covered in Part 1. Part 2 is then a brief tutorial for programming in Python.

### Part 1. K-nearest neighbors
Handwriting recognition refers to a computer’s ability to intelligently interpret handwritten inputs and is broadly applied in document processing, signature verification, and bank check clearing[3]. An important step in handwriting recognition is classification, which classifies data into one of a fixed number of classes according to learning models and training sets. The typical and most popular type of classification is called supervised learning. Specificly, we produce a set of already-classified data as input to a training model[4], which is a hypothesis function to approximate the corresponding problem. During the training process, the model will update the parameters, allowing it to make a reasonable prediction based on the pre-trained hypothesis function. 

With the name “machine learning” coined in 1969 by Arthur Samuel[5], researchers have designed various machine learning algorithms suitable for different type of problems. As one of the earliest machine learning algorithms, KNN has a straightforward and intuitive method to classify data: “similar inputs have similar outputs[6]”.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" width="300">
    <font size="2">
    <figcaption> Figure 1: Scheme in KNN Prediction </a> 
    </figcaption>
    </font>
</figure>

As shown in Figure 1, all points are projected to a 2D hyperplane. Three of them are labeled “+”, and the other three are labeled “-”. How should we classify the new point marked as “?”? Since its nearest neighbors are 2 “+”'s and 1 “-”,we should label it as “+” based on the principle of “similar inputs have similar outputs”.

But what about predicting digits in images? As we all know, all files are stored as numbers in electronic devices, including images. Suppose we have a colored image with low resolution, 28x28. That is, we have 784 pixels in this image. In RGB color mode, each pixel will be represented by three numbers ranging from 0 to 255 and corresponding with the colors red, green, and blue. To simplify our design, images in the training set and the testing set are black and white. Figure 2 shows two examples in the training set.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/HandwrittenDigits.png" width="800">
    <font size="2">
    <figcaption> Figure 2: Training instance for digit 0 (a), training instance for digit 7 (b) </a> 
    </figcaption>
    </font>
</figure>

### Part 2. Google Colab

In this lab, you will be programming in Python, and we will be using Google Colab, which is based off Jupyter Notebook, as it makes it very easy to collaborate with your peers in real-time. Google Colab works very similarly to a Google Docs, propogating changes that you may make on the document on your device, to all other devices that have access to the very same document. Since it is based off of Jupyter Notebook, the files have an extension, ".ipynb," also allowing them to have both text blocks and code blocks. You can run each of the code blocks by clicking on the "run" button on the top left of each of the code blocks. We have chosen this platform, since you can easily play with the code that we have provided for you, after each and every part of the tutorial, and also since it is very convenient for the text explanations to be located right near the code blocks pertaining to the text, so that you can see what we are talking about, right after you read something that was explained in the text. 

Below, at the bottom of the Python tutorial, you will find the link to a folder, containing all the necessary material for lab3. You will first have to choose one person in your group that will copy this folder into his/her own drive, and share it with the rest of your groupmates, so that everyone will be able to edit each of the files. Feel free to make multiple copies of the tutorial if you wish, so that each person in your group can play with the example code simultaneously, without any conflicts.

### Part 3. Python Tutorial
Python, as a high-level programming language for general-purpose programming language, was the most popular programming language in 2017[9]. Most programmers start their coding journal from Python because of its high code readability, clear constructs, syntactically significant whitespace, and abundant open-source standard libraries[10]. Moreover, it supports dynamic automatic memory management and multiple programming paradigms, including object-oriented, imperative, functional and procedural. In this section, we will go over the basic syntax and data structures of Python.

In this part, you should navigate to the copy of the folder you have created and go to the file, "example.ipynb," so that you can follow along with the Python tutorial there.

Link to Folder: https://drive.google.com/drive/folders/1kYCltMJSid-Oc8IZqZsCcOZW1fFxs2nk?usp=sharing

Lab Exercises
--------------------------------

### Part 1. Function Implementation
In this part, you should implement four basic parts for building the digit recognition system. For the first part, we will calculate the hamming distance of training images and the testing image. The second part should then sort the distances to find its K nearest neighbors. The third part will execute a vote for different labels (digits in our case). Finally, we sort the votes and return the final prediction. To get started, first navigate to the file, *digitrec_P1.ipynb*, which should be under the directory, *Python_notebooks*, if you have preserved the original directory structure. You will find any data files that you may need under the directory, *dataset*. You should navigate through the python notebooks, instead of solely relying on this handout, as this handout doesn't go into as much detail as the python notebooks. Before testing, you will have to upload files into your Google Colab document. Please refer to the instructions listed on the document(the section is located at the top of the document), and it will instruct you on how to upload files to the Google Colab VM.

As always, ask a teaching assistant if you need help with any of these parts.

#### Part 1A. Calculate Hamming Distance
First, navigate to the comment section that says, "1.calculate distance". This is where you will implement the first part of this lab assignment. In this part, you will calculate the hamming distance between the test digit(we have already provided this a little further up in the code). Using the methods of the Digit class, try to calculate the hamming distance from the testing digit to each of the training images.

#### Part 1B. Sort Distances
Next, navigate to the comment section that says, "2.sort distances". In this section, we will sort the results list that we have already made in the previous part so that we have the tuples in order of distance, from least to greatest(we would like to find the K-*nearest* neighbors, after all). To simplify this section for you, you may use one of Python's built-in functions, *sorted*, which takes the entire list of tuples, and can sort by whatever you would like to specify it to sort by. In this case, we would like to sort by distance. This will take a little bit of google-ing on your part, so make sure to ask a teaching assistant if you need any help. If you have prior coding experience, you may be interested in trying out the extension, which implements the same sorting algorithm that Python uses in its built-in function called "Adaptive Merge Sort". Through doing this exercise, you will learn about a new programming archetype called recursion. Be sure to complete the entirety of this lab before coming back to try this optional extension.

#### Part 1C. KNN Vote
In this section, you will find the K-nearest neighbors of the testing image, and store them in a dictionary with their label as keys and the number of digits with that label as their value. For this reason, your loop will only iterate K times and not over the entire list. You will find the section you have to implement under the comment "3.knn vote". 

#### Part 1D. Sort Vote
In this part, you will sort the dictionary that you just created. Feel free to search the internet on how you can sort a dictionary(make sure you know whether you want to sort the dictionary by keys or values). And as always, ask a teaching assistant if you're having trouble. When you think you have correctly implemented all four parts, you may check your code using the provided test harness. You can do so by using the terminal to run the test script. Once you have navigated to the correct directory, use *python main.py* to run the test cases. If you need any help debugging after any failed test cases, feel free to ask a teaching assistant. Just as in lab 2, remember to check the syntax of your code very carefully-- it is likely that many failed test cases are due to syntax errors!


```diff
- Sign-Off Milestone: 
Once you have passed all the test cases provided in the test harness, show the code and results to one of the TAs before moving on.
```

### Part 2. Verify Digit Recognition System Locally
After passing all check points done by the test harness, you can move to *digitrec_P2.ipynb* – a more convincible verification of the digit recognition system. In this part, you can simply copy and paste the code you implemented in Part 1. If the error rate is smaller than 10%, then you can move on to Part 3. Make sure that you are pasting correctly, as it is very easy to miss some parts and get errors that could potentially be difficult to debug.

```diff
- Sign-off Milestone: 
Once you have achieved an error rate smaller then 10%, show the code and results to one of the TAs before moving on.
```

### Part 3. Deploy Digit Recognition Web Application
Now it’s time to deploy a web application based on your digit recognition system. Open a browser and type in the IP address “10.XX.XX.XX”. Then type in your Username and Password to log into the system. After that, please double check that the group number shown at the top is correct. Before starting to draw on the canvas, you will have to upload a python file that contains the code you wrote part2. You can paste each of the parts into a python file, before uploading it to the system. Afterwards, test your system by drawing digits(or other things if you'd like), to see whether it works as expected.

```diff
- Sign-off Milestone: 
Once you have verified your web app, demonstrate the final web-based digit recognition system to one of the TAs.
```

### Extensions
In this extension, we will implement a specific type of sort, called "adaptive merge sort"[12]. This is the same sort method that the built in python method, *sorted* uses when it sorts things like lists and dictionaries. Through implementing this sort method, you will learn about a programming archetype called recursion, and also a little bit about the process behind making an algorithm like this one. To make this function, you will need to make three separate functions, all of which have comment blocks over them. 

The first funciton will be the "main" function that will use recursion. In this function, you will have, a base case. This occurs when the size of the list is small enough that you know the answer right off the bat. In this case, a list with only one element will always be sorted. Then, you will move onto the recursive case. First, you will partition the array into two halves. The first sub-array will contain all even-indexed elements in the array, while the second sub-array will contain all odd-indexed elements. If we happen to be lucky and the two of these array happen to be already sorted, we can proceed to merge the sorted arrays together(our second function will check whether these two sub-arrays are sorted, and our third function will merge two sorted arrays together, into one sorted array). In the rest of our "main" function, we either return the sorted array after merging, if we got "lucky" or we recurse on the two halves that we made, and sort in the same way. Notice that this recursion will terminate due to the base case. If we didn't have the base case there, we would get an 'indexOutOfBounds' error, which would mean that we tried to access a list element that's not actually in the list(one that's either before the first element, or past the last element). To prevent this from happening, we must have a base case. Always make sure that when using recursion, you are making the problem progressively smaller as well.

Implement the three functions that are located in the comment block that says, "EXTENSION". This extension is fairly difficult, so make sure to ask a teaching assistant if you need any help. Do not be discouraged if you cannot do this extension! It is much harder than the rest of the lab and is meant only as an optional challenge. Once you have finished, you may first test your work on your own, using the same testing suite that was provided. Then, you may also connect to our server once more to test the program using your own hand-written digits. Once both of these work, you can show your results to a teaching assistant, so that they can sign-off on your work.

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
