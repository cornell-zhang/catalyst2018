Lab 3: Handwritten Digit Recognition
======================
Why should we explore machine learning applications? The answer seems obvious: we want machines to complete hard work for us. With the significant improvement of the computing ability of electronic devices in recent years, machine learning has become a key technique for solving problems in various areas, including image/video processing, computational biology, the automotive industry, aerospace engineering, and manufacturing. It is a data analytics technique that teaches computers to do what comes naturally to human beings: learn from experience[1]. By leveraging machine learning algorithms to train digital systems, they can extract useful information (features) intelligently from huge amounts of data, which releases people from these trivial tasks. One of the most well-known machine learning applications is handwritten digit recognition.

In the last lab, you built a smart robot that can search and find a target. Now let's make it even more smart by building a brain for the robot! And in the projects, you will be able to control the robot using this system. In this lab assignment, you and your partner will explore digital intelligence by implementing a handwritten digit recognition system using Python – an interpreted high-level programming language, and the machine learning algorithm that we will be using here, is called K-nearst-neighbors (KNN), which will be introduced in the next section - software description. The first part of this section describes the algorithm for the digit recognition system, that is K-nearst-neighbors(KNN). Then the second part introduces Google Colab-- an online Google Drive based Python IDE. The final part includes a Google Colab based Python notebook, which will serve as a tutorial and will cover basic usage and a detailed explanation of the Python elements you will need for this lab. If you are new to Python, please spend as much time as you need, so that you understand each of the different parts, as you will likely be using many of those concepts to implement your digitrec system. As for the lab exercises, the first three parts require you implement and verify fundamental functions includes calculating distances, sorting distances, and voting for the final result/prediction. Then, you can move to the fourth part and build the digit recognition system. After achieving an error rate lower than 10%, you will move to the last part: upload your code to the remote server and randomly draw digits on the canvas to further test your design.

Software Description
--------------------------------

Before getting started with implementing your digitrec system, you should read this section carefully to learn basic knowledge about KNN and Python. In this section, the motivation for machine learning applications and the methodology of machine learning algorithms will be covered in part 1. Then part 2 will contain a brief introduction to Google Colab, which is the online platform to program and test python scripts. Lastly, part 3 is a tutorial for programming in Python(it will be an interactive tutorial that you can play around with, on a Google Colab document, *example.ipynb*).

### Part 1. K-nearest neighbors
Handwritten digit recognition refers to a computer’s ability to intelligently interpret handwritten inputs and is broadly applied in document processing, signature verification, and bank check clearing[3]. An important step in handwritten recognition is classification, which classifies data into one of a fixed number of classes according to learning models and training sets(already classified handwritten digits). The typical and most popular type of classification is called supervised learning, which involves learning to make a prediction from data. Specificly, we produce a set of already classified data(training data set) as input to a training model[4], which is a hypothesis function to approximate the corresponding problem. During the training process, the model will update the parameters, allowing it to make a reasonable prediction based on the pre-trained hypothesis function. 

With the name “machine learning” coined in 1969 by Arthur Samuel[5], researchers have designed various machine learning algorithms suitable for different types of problems. As one of the earliest machine learning algorithms, KNN has a straightforward and intuitive method to classify data, based on the principle: “similar inputs have similar outputs[6]”.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" width="300">
    <font size="2">
    <figcaption> Figure 1: Scheme in KNN Prediction </a> 
    </figcaption>
    </font>
</figure>

As shown in Figure 1, all points are projected to a 2D hyperplane. Three of them are labeled “+”, and the other three are labeled “-”. How should we classify the new point marked as “?”? Since its nearest neighbors are 2 “+”'s and 1 “-”,we should label it as “+” based on the principle of “similar inputs have similar outputs”.

But what about predicting handwritten digits in images? As you may know, all files are stored as numbers in electronic devices, including images. For colored images under RGB mode, each pixel will be represented by three numbers ranging from 0 to 255 which corresponding to the colors: red, green, and blue. To simplify our design, images in the training set and the testing set are black and white, that is only "0" or "1" for each pixel. Figures 2 and 3 shows two simple examples of training instances with a resulution of 7x7, and we will use similar inputs to test your code modularly(each function separately), once you implement each one.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/2.1.PNG" width="800">
    <font size="2">
    <figcaption> Figure 2: Training instance for digit 0 - resolution 7x7 </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/2.2.PNG" width="800">
    <font size="2">
    <figcaption> Figure 3: Training instance for digit 7 - resolution 7x7 </a> 
    </figcaption>
    </font>
</figure>

With the training set and testing set stored in the format of a binary array, we could classify the testing instances by referring to the rule "similar inputs have similar outputs." To evaluate the similarity between the testing instance and training instance, we could calculate the hamming distance[7], which is defined as the total number of corresponding bits that are different in the two binary strings. For example, 1011 and 0111 differ in the two most significant(bits on the left of the string) bits and therefore have a distance of 2. 1011 and 1010 differ only in the least significant(bits on the right of the string) bit and have a distance of 1. As a result, 1011 is closer to 1010 than to 0111. To implement the function of calculating the hamming distance, we use the XOR logic (represented as "^" in Python) you have experienced with in lab 1.

However, these simple images shown before are not enough to build an accurate handwritten digit recognition system. More features (training images with a higher resolution) and a large number of training images are required to build a realtively well-performing handwriten digit recognition system. Thus we use part of the well-known MNIST dataset with a resolution of 28x28 in the part 4 of the lab exercise. Again to simplify the design, images in the training set and the testing set are preprocessed to black and white ones. Figure 4 shows two digits with the resolution of 28x28. To guarantee the accuracy of predicting random handwritten digits on the canvas in part 5 of the lab exercise, the deployed web application utilizes the whole MNIST dataset and some additional corner instancecs that we have added to that data set.  

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/HandwrittenDigits.png" width="800">
    <font size="2">
    <figcaption> Figure 4: Training instance for digit 0 (a), training instance for digit 7 (b) - resolution 28x28 </a> 
    </figcaption>
    </font>
</figure>

### Part 2. Google Colab

In this lab, you will be programming in Python, and we will use Google Colab, which is based on the Jupyter Notebook IDE, as it makes it very easy to collaborate with your peers in real-time. You should have a Google account to use it. To get started, please click the following link to the shared folder and copy all files inside this folder to your Google Drive. You could select all of them and right click the mouse and choose the item "Make a copy" (Figure 5). After doing so, you will want to have these files in the same folder, so that you can easily access them. Make sure to select all these files in your personal Google Drive, and move them into a folder that you will create. You may need to search for them in the search bar, if you have many files in your Drive already.

Link to Folder: https://drive.google.com/drive/folders/1kYCltMJSid-Oc8IZqZsCcOZW1fFxs2nk?usp=sharing

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/5.png" width="800">
    <font size="2">
    <figcaption> Figure 5: Copy all files to your own drive </a> 
    </figcaption>
    </font>
</figure>

Google Colab works very similarly to a Google Docs, propogating changes that you may make on the document on your device, to all other devices that have access to the very same document. Since it is based on Jupyter Notebook, the files have an extension, ".ipynb,". To open these files from your Google Drive, you can either double click the file and click the column in the top named "Open with Colaboratory" (Figure 6) or choose the file, right click the mouse and select the item "Open with Colaboratory" (Figure 7).

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/6.png" width="800">
    <font size="2">
    <figcaption> Figure 6: Open python notebook using Google Colab - w1 </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/7.png" width="800">
    <font size="2">
    <figcaption> Figure 7: Open python notebook using Google Colab - w2 </a> 
    </figcaption>
    </font>
</figure>

Notebooks in Google Colab are allowed to have both text blocks and code blocks. You can run the code blocks by clicking on the "run" button on the top left of each code blocks (Figure 8). We have chosen this platform, since you can easily play with the code that we have provided for you, after each and every part of the tutorial, and also since it is very convenient for the text explanations to be located right near the code blocks pertaining to the text, so that you can see what we are talking about, right after you read something that was explained in the text. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/8.png" width="800">
    <font size="2">
    <figcaption> Figure 8: Run code by clicking the "run" button in the left side of the code cell </a> 
    </figcaption>
    </font>
</figure>

### Part 3. Python Tutorial
Python, as a high-level programming language for general-purpose programming language and was ranked as the most popular programming language in 2017[9]. These days, most students start their coding journal from Python because of its high code readability, clear constructs, syntactically significant whitespace, and abundant open-source standard libraries[10].In this section, we will go over the basic syntax and data structures of Python.

In this part, you should navigate to the copy of files in the shared folder (link available in the last section). Please open the file named *example.ipynb*, so that you can follow along with the Python tutorial there. To effectively learn Python from practice, feel free to modify and run the example notebook. If you accidentally mess it up, you could easily recover it by re-copying the original notebook in the shared folder.

Lab Exercises
--------------------------------

In this section, you should implement four basic parts for building the digit recognition system. For the first part, we will calculate the hamming distance between the training images and the testing image. The second part should then sort the distances to find its K nearest neighbors. The third part will execute a "vote" on digits, to see which one is most represented in the K-Nearest Neighbors, to return as the final result. To get started, first navigate to the file called *digitrec.ipynb*. There, you will find each of the parts below, along with a description of each part you will have to implement. The five parts in the file correspond to the parts that are below-- in this handout. The file includes comment blocks as well as comments within the code, so make sure to read through the comment blocks before attempting a given part. The first three parts will involve you implementing functions, while the fourth part will involve testing the accuracy of your system, and the fifth part will involve uploading your file to our server, so that you can test out your code for yourself. For part 4, we will use a reduced MNIST training dataset named *dataset.csv*, and for part 5, we will use the entire file. In this part, you will just have to copy the functions that you will have implemented in the Google Colab document, and transfer them to the file, *digitrec_sol.py*, which can be found in the Google Drive folder. You should navigate through the python notebooks, instead of solely relying on this handout, as this handout doesn't go into as much detail as the python notebooks. Before testing(only for part 4), you will have to upload files into your Google Colab document. Please refer to the instructions listed on the document(the section is named part 4(a)), and it will instruct you on how to upload files to the Google Colab virtual machine (VM).

As always, ask a teaching assistant if you need help with any of these parts.

### Digit Class
In this preliminary part, you will explore the class structure of the Digit class. If you need a refresher on classes and objects, you may refer to the tutorial in *example.py*. Take note of the data members and functions of the class, as you will be working with Digit objects throughout this lab.

### Part 1. Calculate Hamming Distance
First, navigate to the comment section that says, "Part 1: Calculate Hamming Distance". This is where you will implement the first part of this lab assignment. In this part, you will calculate the hamming distance between the test digit(we have already provided this a little further up in the code), and each of the digits in the training set. 

*HINT*: This method can be implemented very elegantly, if you exploit the methods of the Digit class.

```diff
- Sign-Off Milestone: 
Once you have implemented this function and compared your results with the correct ones that we have provided for you, show the results of your function to a TA before moving on.
```

### Part 2. Sort by Hamming Distance
Next, navigate to the comment section that says, "Part 2: Sort by Hamming Distance". In this section, we will sort the results list that we have already made in the previous part so that we have the tuples in order of hamming distance, from least to greatest(we would like to find the K-*nearest* neighbors, after all). To simplify this section for you, you may use one of Python's built-in functions, *sorted*, which takes the entire list of tuples, and can sort by whatever you would like to specify it to sort by. A simple example was provided to you in the tutorial, so you may refer to that if you are stuck. Also, this may take a little bit of google-ing on your part, so make sure to ask a teaching assistant if you need any help. If you have prior coding experience, you may be interested in trying out the extension, which implements the same sorting algorithm that Python uses in its built-in function called "Adaptive Merge Sort". Through doing this exercise, you will learn about a new programming archetype called recursion. Be sure to complete the entirety of this lab before coming back to try this optional extension.

```diff
- Sign-Off Milestone: 
Once you have finished sorting the results of your previous funciton, check the results of your function against the correct sorted result list that we have provided for you. Once you have finished, be sure to show your results to a TA before moving on.
```

### Part 3. Find K-Nearest Neighbors
In this section, you will find the K-nearest neighbors of the testing image, and store them in a dictionary with their label as keys and the number of digits with that label as their value. For this reason, your loop will only iterate K times and not over the entire list. After doing this, you will have to sort this dictioary by frequency of the digits. This way, we can pick out the digit with the highest frequency as our final result. You will find the section you have to implement under the comment "Part 3: Find K-Nearest Neighbors". 

```diff
- Sign-Off Milestone: Once you have implemented this function, compare your results with the correct labelMap that we have provided for you. After verifying the correctness of your function, be sure to have a TA verify your results before moving on.
```

### Part 4. Combining Functionality and Testing for Accuracy
After checking your implementation for each of the methods from the first three parts, you will use this part to combine their functionalities and build your entire digitrec system. In this part, we have provided some training data for you, that is in the Google Drive folder that you have access to. You will use the copied file, *dataset.csv*, to provide training and testing images to test the accuracy of your system. To allow your program to access the data file, you will have to first upload the file to your Google Colab Virtual Machine(VM). Follow the instructions in part 4(a) to upload this file into the VM. Once you have uploaded the file, change the "filename" field in the code, so that the code can load the digit images from this file. Once you have done so, you will be able to run your digitrec system. Notice that, in the "digitrec" function, we make function calls to the other methods that you have implemented before. In this way, we have combined our modular design into a fully functional digitrec system. After doing all this, you will implement a function that finds the accuracy of the classifications that your digitrec system outputs, by comparing those outputs with the correct ones. This will be done in section 4(b). Lastly, you will combine all these parts together into your digitrec system, using the accuracy rate function that you implemented in the previous part, to find the success rate of your implementation.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/9.png" width="800">
    <font size="2">
    <figcaption> Figure 9: Get Shareable Link </a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/10.png" width="800">
    <font size="2">
    <figcaption> Figure 10: Copy the link to a window of Chrome and get the fileID </a> 
    </figcaption>
    </font>
</figure>

```diff
- Sign-off Milestone: 
Once you have achieved an error rate smaller then 10%, show the code and results to one of the TAs before moving on.
```

### Part 5. Deploy Digit Recognition Web Application
Now it’s time to deploy a web application based on your digit recognition system. Please open "Chrome" and type in the IP address “132.236.59.106” or the domain name "zhang-precision-02.ece.cornell.edu" to access our server. According to your group number, your username will be "gX", where "X" is your group number, i.e. g1,g2,g5,etc. and your password will be the same as your username. Hit the "Login" button once you have filled these two fields. Please double check that the group number shown on the top(after the login screen) is correct. Before starting to draw on the canvas, you will have to upload a python file that contains the code you wrote in the first part. Please go back to the shared file, download the template called *digitrec_sol.py* into your local machine. Then open it within any programming IDE you like and paste the functions you implemented before, into the correct place. After having done so, upload the file *digitrec_sol.py*, which includes your solution/implementation, to the server by clicking the button "upload python script". Lastly, you can test your system by drawing digits(or other things if you'd like), to see whether your system works as expected.

```diff
- Sign-off Milestone: 
Once you have verified your web app, demonstrate the final web-based digit recognition system to one of the TAs.
```

### Extensions
In part 2, you implement the sort distances function by applying the python built-in function called sort(). You may ask the question: what's going on? why it just worked? Actually there are many different sorting algorithms, so if you are interested, please go ahead and check out this nice 6 minute video!

https://www.youtube.com/watch?v=kPRA0W1kECg

Sorting algorithms are so important that many reserchers are still focusing on it. Thus in this extension, you will learn the algorithm called "adaptive merge sort"[12] used in the python build-in function sort().Through implementing this sort method, you will learn about a programming archetype called recursion, and also a little bit about the process behind making an algorithm like this one. To make this function, you will need to make three separate functions, all of which have comment blocks over them. 

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
