Lab 3: Handwritten Digit Recognition
======================
Why should we explore machine learning applications? The answer seems obvious: we want machines to complete hard work for us. With the significant improvement of the computing ability of electronic devices in recent years, machine learning has become a key technique for solving problems in various areas, including image/video processing, computational biology, the automotive industry, aerospace engineering, and manufacturing. It is a data analysis technique that teaches computers to do what comes naturally to human beings: learn from experience [1]. By leveraging machine learning algorithms to train digital systems, they can extract useful information (features) intelligently from huge amounts of data, which relieves people from these tedious tasks. One of the most well-known machine learning applications is handwritten digit recognition, which we'll be doing in this lab.

In the last lab, you built a smart robot that can search and find a target. Now let's make it even smarter by building a brain for the robot! And in the projects, you will be able to control the robot using this system. In this lab assignment, you and your partner will explore digital intelligence by implementing a handwritten digit recognition(digitrec) system using Python-- an interpreted high-level programming language. The machine learning algorithm that we will be using here is called K-Nearest Neighbors (KNN), which will be introduced in the next section. The first part of this section describes the KNN algorithm. Then the second part introduces Google Colab-- an online Google Drive based Python IDE. The final part includes a Google Colab based Python notebook, which will serve as a tutorial and will cover basic usage and a detailed explanation of the Python elements you will need for this lab. If you are new to Python, please spend as much time as you need, so that you understand each of the different parts, as you will likely be using many of those concepts to implement your digitrec system. As for the lab exercises, the first three parts require you implement and verify fundamental functions including calculating distances, sorting distances, and voting for the final result/prediction. Then, you can move to the fourth part and build the digit recognition system by combining all the previous parts. After achieving an error rate lower than 10%, you will move to the last part: upload your code to the remote server and randomly draw digits on the canvas to further test your design.

Software Description
--------------------------------

Before getting started with implementing your digitrec system, you should read this section carefully to get a basic understanding about KNN and Python. In this section, the motivation for machine learning applications and the methodology of machine learning algorithms will be covered in part 1. Then part 2 will contain a brief introduction to Google Colab, which is the online platform to program and test Python scripts. Lastly, part 3 is a tutorial for programming in Python (it will be an interactive tutorial that you can play around with on a Google Colab document, *example.ipynb*).

### Part 1. K-Nearest Neighbors
Handwritten digit recognition refers to a computer’s ability to intelligently interpret handwritten inputs and is broadly applied in document processing, signature verification, and bank check clearing [2]. An important step in handwritten digit recognition is classification, in which the algorithm classifies data into one of a fixed number of classes according to training sets (already classified handwritten digits).  

With the name “machine learning” coined in 1969 by Arthur Samuel [4], researchers have designed various machine learning algorithms suitable for different types of problems. As one of the earliest machine learning algorithms, KNN has a straightforward and intuitive method to classify data, based on the principle: “similar inputs have similar outputs” [5].

First, we will describe the KNN algorithm, and afterwards, provide an example, so that you can further solidify your understanding of the algorithm. By doing this, you can start to get an idea of the process that you will have to implement through Python code, when doing this lab yourself. To start, the algorithm will first sort the "training set" (the set of instances that you already have classified, which you will be using to classify a "testing instance") by using their "distance" (which will be referred to as the hamming distance) to the "testing instance". After having sorted these "training instances," the algorithm will choose the first K (where K is usually chosen by the specific use case) of these "training instances" (these are the K-Nearest "training instances" to our "testing instance") to use to classify our "testing instance". Since these "training instances" have already been classified (given a label, containing the category the instance is a part of), the algorithm will consider each of these instances to have one vote. This vote will consist of the label that the particular "training instance" has been classified as. At the end, the label with the most votes will be chosen to be the label of the "testing instance". Therefore, the "testing instance" will be put in the category with the most votes at the end of the algorithm. Below, we give a pictorial representation of this process, with K = 3.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/KNNPrediction.png" width="300">
    <font size="2">
    <figcaption> Figure 1: Scheme in KNN Prediction  <br><br></a> 
    </figcaption>
    </font>
</figure>

As shown in Figure 1, all points (corresponding to data, which we will assume are 2D) are projected onto a plane. Three of them are labeled “+”, and the other three are labeled “-” (this means that there are two categories for that we could possibly classify into, "+" or "-"). How should we classify the new point marked as “?”? Since we are using K=3, and since its 3 nearest neighbors are 2 “+”'s and 1 “-”, we should label it as “+”, as "+" would have two votes in this case, while "-" would only have one, and thus, "+" would win out.

But what about predicting handwritten digits in images? As you may know, all files are stored as numbers in electronic devices, including images. For colored images under RGB (Red, Green, Blue) mode, each pixel will be represented by three numbers ranging from 0 to 255 which would correspond to the colors: red, green, and blue, in that order. This means that if one pixel was represented as "(50, 200, 15)", the pixel's color would consist of 50 parts red, 200 parts green, and 15 points blue. To simplify our design, in this lab, however, images in the training set and the testing set will be black and white-- that is only "0" or "1" for each pixel. Figures 2 and 3 show two simple examples of training instances with a resolution of 7x7, and we will use similar inputs to test your code modularly (each function separately), once you implement each one.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/DigitRepOne.png" width="800">
    <font size="2">
    <figcaption> Figure 2: Training instance for digit 0 - resolution 7x7 <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/DigitrRepTwo.png" width="800">
    <font size="2">
    <figcaption> Figure 3: Training instance for digit 7 - resolution 7x7 <br><br></a> 
    </figcaption>
    </font>
</figure>

With the training set and testing set stored in the format of a binary array, we could classify the testing instances by referring to the rule "similar inputs have similar outputs." To evaluate the similarity between the testing instance and training instance, we could calculate the hamming distance[6], which is defined as the total number of corresponding bits that are different in the two binary strings. For example, 1011 and 0111 differ in the two most significant(bits on the left of the string) bits and therefore have a distance of 2. 1011 and 1010 differ only in the least significant(bits on the right of the string) bit and have a distance of 1. As a result, 1011 is closer to 1010 than to 0111. To implement the function of calculating the hamming distance, we use the XOR logic (represented as "^" in Python) you have experienced within lab 1.

However, these simple images shown before are not enough to build an accurate handwritten digit recognition system. More features (training images with a higher resolution) and a large number of training images are required to build a relatively well-performing handwritten digit recognition system. Thus we use part of the well-known MNIST dataset with a resolution of 28x28 in part 4 of the lab exercise. Again to simplify the design, images in the training set and the testing set are preprocessed to black and white ones. Figure 4 shows two digits with the resolution of 28x28. To guarantee the accuracy of predicting random handwritten digits on the canvas in part 5 of the lab exercise, the deployed web application utilizes the whole MNIST dataset.  

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/HandwrittenDigits.png" width="800">
    <font size="2">
    <figcaption> Figure 4: Training instance for digit 0 (a), training instance for digit 7 (b) - resolution 28x28 <br><br></a> 
    </figcaption>
    </font>
</figure>

### Part 2. Google Colab

In this lab, you will be programming in Python, and to do this, we will be using Google Colab-- based on the Jupyter Notebook IDE-- as it makes it very easy to collaborate with your peers in real-time. You need to have a Google account to use Google Colab, so if you don't already have one, you should make one before coming in to complete this lab. To get started, please first login to your account and go to your Google Drive homepage. Then, use the link below to obtain the folder that will contain all the files you will need for this lab. Next, copy all the files within this folder into your Google Drive. You will have to select all of them and right click the mouse and choose the item "Make a copy" (Figure 5), since Google Drive won't let you copy entire folders to your Drive. After doing so, you will probably want to have these files in the same folder, so that you can easily access them. Make sure to select all these files in your personal Google Drive, and move them into a folder that you will create. You may need to search for them in the search bar if you have many files in your Drive already. After placing them all into their own folder on your Drive, you will also want to rename the files, since their names will become something like, "Copy of \_\_\_\_\_\_", once you copy them. When you rename them, you should use the name of the original file, followed by, "--GroupX", where you can replace "X" with the number of your group. This way, if you are having any trouble, you can share your document with one of the TA's, and he/she will know exactly which document is yours.

<a href="https://drive.google.com/drive/folders/1kYCltMJSid-Oc8IZqZsCcOZW1fFxs2nk?usp=sharing"> Link to Folder </a> 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/5.png" width="800">
    <font size="2">
    <figcaption> Figure 5: Copy all files to your own drive <br><br></a> 
    </figcaption>
    </font>
</figure>

Google Colab works very similarly to a Google Docs, propagating changes that you may make on the document on your device, to all other devices that have access to the very same document. Since it is based on Jupyter Notebook, the files have the extension ".ipynb". To open these files from your Google Drive, you can either double-click the file and click the column in the top named "Open with Colaboratory" (Figure 6) or choose the file, right-click the mouse and select the item "Open with Colaboratory" (Figure 7).

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/6.png" width="800">
    <font size="2">
    <figcaption> Figure 6: Open Python Notebook using Google Colab -- First Way <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/7.png" width="800">
    <font size="2">
    <figcaption> Figure 7: Open Python Notebook using Google Colab -- Second Way <br><br></a> 
    </figcaption>
    </font>
</figure>

Notebooks in Google Colab are allowed to have both text blocks and code blocks. You can run the code blocks by clicking on the "run" button on the top left of each code blocks (Figure 8). We have chosen this platform, since you can easily play with the code that we have provided for you, after each and every part of the tutorial, and also since it is very convenient for the text explanations to be located right near the code blocks pertaining to the text, so that you can see what we are talking about, right after you read something that was explained in the text. 

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/8.png" width="800">
    <font size="2">
    <figcaption> Figure 8: Run code by clicking the "run" button in the left side of the code cell <br><br></a> 
    </figcaption>
    </font>
</figure>

### Part 3. Python Tutorial
Python, as a high-level programming language for general-purpose programming language and was ranked as the most popular programming language in 2017 [8]. These days, most students start their coding journey using Python because of its high code readability, clear constructs, syntactically significant whitespace, and abundant open-source standard libraries [10]. In this section, we will go over the basic syntax and data structures of Python.

In this part, you should navigate to the copy of files in the shared folder (link available in the last section). Please open the file named *example.ipynb*, so that you can follow along with the Python tutorial there. To effectively learn Python from practice, feel free to modify and run the example notebook. If you accidentally mess it up, you could easily recover it by re-copying the original notebook in the shared folder.

Lab Exercises
--------------------------------

In this section, you should implement three basic functions for building the digit recognition system. For the first function, we will calculate the hamming distance between the training images and the testing image. The second function should then find the K of these training images that have the lowest hamming distance to the testing image. The third function will execute a "vote" on digits, to see which label is most represented, and it will return that label as the final classification. Don't worry if all these parts don't make complete sense to you right now-- you'll get the hang of it as you follow along in the python notebook. To get started, first navigate to the file called *digitrec.ipynb*, in the Google Drive folder. There, you will find each of the parts below, along with a description of each part you will have to implement. The five parts in the file correspond to the parts that are below in this handout. You should note that the python notebook file includes much more detail than this handout, so be sure to read through both the text blocks and the comments within the code, before beginning to implement each part. We have included a preliminary part to make you comfortable with the way we will be representing digits here. The next three parts will involve you implementing functions, while the fourth part will involve testing your system on various inputs, and culminating with you finding accuracy of your system. Lastly, the fifth part will involve uploading your file to our server, so that you can test out your code for yourself. For part 4, we will use a reduced MNIST training dataset named *dataset.csv*, and for part 5, we will use the entire file. In this part, you will just have to copy the functions that you will have implemented in the Google Colab document, and transfer them to the file, *digitrec_template.py*, which can be found in the Google Drive folder. Before testing (only for part 4), you will have to upload files into your Google Colab document. Please refer to the instructions listed on the document (the section is named part 4(a)), and it will instruct you on how to upload files to the Google Colab virtual machine (VM).

As always, ask a teaching assistant if you need help with any of these parts.

### Digit Class
In this preliminary part, you will explore the class structure of the Digit class. If you need a refresher on classes and objects, you may refer to the tutorial in *example.ipynb*. Take note of the data members and functions of the class, as you will be working with Digit objects throughout this lab. After looking through the Digit Class, you will be asked to complete a few short exercises in the code block that follows it.

```diff
-Sign-Off Milestone-
```
Once you have completed the exercises, show your results to a TA before moving on.

### Part 1. Calculate Hamming Distance
First, navigate to the text section that says, "Part 1: Calculate Hamming Distances". This is where you will implement the first part of this lab assignment. In this part, you will calculate the hamming distance between the test digit (we have already provided this a little further up in the code), and each of the digits in the training set. In part (a) of this section, you will explore the *distance* method of the Digit class. Afterwards, you will implement the main function in this section, and lastly, you will test the results of that function. You will find further detail in the text section and in the comments that we provided you in the function. After finishing, move on to testing to see whether your function works correctly.

```diff
-Sign-Off Milestone-
```
Once you have implemented this function and verified your results with the simple inputs that we have provided for you, show your results to a TA before moving on.

### Part 2. Find K-Nearest Neighbors
Next, navigate to the text section that says, "Part 2: Find K-Nearest Neighbors". In this section, you will find the K-Nearest Neighbors of the testing image, based on their hamming distances. These K-Nearest Neighbors don't need to be sorted by distance. This section is much more complicated that the last, so make sure to read through both the text block and the comments in the code block right after that for more detail. If you have any questions, be sure to ask a TA. After finishing, move on to testing to see whether your function works correctly.

```diff
-Sign-Off Milestone-
```
Once you have finished sorting the results of your previous function, check the results of your function using the simple inputs we have provided for you. Once you have finished, be sure to show your results to a TA before moving on.

### Part 3. Find Classification
Now, navigate to the text section that says, "Part 3. Find Classification". In this section you will use the output from the previous function you implemented, and vote on labels for the training images in your list. After doing so, you will iterate through these labels, picking out the one with the most votes to return from the function. For more detail please refer to both the text block and the comments in the code block of the function you are implementing for this part. After finishing this part, test to see that your function works properly, before showing your results to a TA.

```diff
-Sign-Off Milestone-
```
Once you have implemented this function, use the provided code to print out your results, and verify the correctness of your function yourself. Be sure to show your results to a TA once you have finished.


### Part 4. Combining Functionality and Testing for Accuracy
After checking your implementation for each of the methods from the first three parts, you will use this part to combine their functionalities and build your entire digitrec system. In this part, we have provided some training data for you that is in the Google Drive folder that you have access to. You will use the copied file, *dataset.csv*, to provide training and testing images to test the accuracy of your system. To allow your program to access the data file, you will have to first upload the file to your Google Colab Virtual Machine (VM). Follow the instructions in part 4(a) to upload this file into the VM (there are images below of what you should be doing). The text box tells you to get the fileID of the file you would like to upload. You may refer to the images below, which show how you can get the fileID of a file on Drive. Once you have done so, you will be able to run your digitrec system. Notice that, in the "digitrec" function, we make function calls to the other methods that you have implemented before. In this way, we have combined our modular design into a fully functional digitrec system. You will first test your digitrec implementation with just one testing image, and then with a few testing images. After doing all this, you will implement a function that finds the accuracy of the classifications that your digitrec system outputs, by comparing those outputs with the correct ones. This will be done in section 4(d) and testing will be done in 4(e). Lastly, you will combine all these parts together into your digitrec system, using the accuracy rate function that you just implemented in the previous part, to find the success rate of your implementation. For more detail, please refer to the Google Colab document.

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/9.png" width="400">
    <font size="2">
    <figcaption> Figure 9: Get Shareable Link by Right-Clicking on File <br><br></a> 
    </figcaption>
    </font>
</figure>

<figure>
    <img src="https://github.com/cornell-zhang/catalyst2018/blob/master/lab3/figures/10.png" width="800">
    <font size="2">
    <figcaption> Figure 10: Copy the link to a window of Chrome and get the fileID <br><br></a> 
    </figcaption>
    </font>
</figure>

```diff
-Sign-Off Milestone-
```
Once you have achieved an error rate smaller than 10%, show the code and results to one of the TAs before moving on.


### Part 5. Deploy Digit Recognition Web Application
Now it’s time to deploy a web application based on your digit recognition system. Please open "Chrome" and type in the IP address “132.236.59.106” or the domain name "zhang-precision-02.ece.cornell.edu" to access our server. According to your group number, your username will be "gX", where "X" is your group number, i.e. g1, g2, g5, etc. and your password will be the same as your username. Hit the "Login" button once you have filled these two fields. Once you have logged in, please double-check that the group number shown on the top (after the login screen) is correct. Before starting to draw on the canvas, you will have to upload a Python file that contains the code you wrote in the first part. Please go back to the shared file, download the template called *digitrec_sol.py* into your local machine. Then open it within any programming IDE you like and paste the functions you implemented before into the correct place. After having done so, upload the file *digitrec_template.py*, which includes your solution/implementation, to the server by clicking the button, "upload_python_script" and then "upload" once you have selected the right file. Lastly, you can test your system by drawing digits (or other things if you'd like) to see whether your system works as expected.

You should note that if you want to connect to the server and play with your handwritten digit recognition system using other electronic devices, say your smartphone, it should be connected to the Cornell network, or else the firewall will block your request.

```diff
-Sign-Off Milestone-
```
Once you have verified your web app, demonstrate the final web-based digit recognition system to one of the TAs.


### Extensions
In part 2, you implement the sort distances function by applying the Python built-in function called sorted(). You may ask the question: what's going on? why it just worked? Actually there are many different sorting algorithms, so if you are interested, please go ahead and check out this nice 6 minute video!

https://www.youtube.com/watch?v=kPRA0W1kECg

Sorting algorithms are so important that many researchers are still focusing on it. Thus in this extension, you will experience the the Python built-in function sorted() which is developed with the algorithm called "adaptive merge sort" [11]. Please refer to the sixth section in the "example.ipynb".

### References
[1] “What is Machine Learning? 3 things you need to know” Available at https://www.mathworks.com/discovery/machine-learning.html

[2] ECE 5775 lab2 handout: Digit Recognition System (Part1). Available at http://www.csl.cornell.edu/courses/ece5775/schedule.html

[3] K-Nearest-Neighbors and Handwritten Digit Classification. Available at:
https://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classification/

[4] Machine Learning – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Machine_learning

[5] CS5780 lecture 2 handout: K-nearest-neighbors. Available at:
http://www.cs.cornell.edu/courses/cs4780/2018sp/page16/index.html

[6] Hamming distance – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Hamming_distance

[7] The MNIST Database of handwritten digits. Available at:
http://yann.lecun.com/exdb/mnist/

[8] Python Tops 2017’s Most popular Programming Languages. Available at:
https://www.extremetech.com/computing/252987-python-tops-list-2017s-popular-programming-languages

[9] Python (programming language) – Wikipedia. Available at:
https://en.wikipedia.org/wiki/Python_(programming_language)

[10] The Python Tutorial. Available at:
https://docs.python.org/3/tutorial/index.html

[11] Adaptive Merge Sort. Available at:
https://www.cs.waikato.ac.nz/~tcs/COMP317/adaptivesort.html
