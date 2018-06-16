#######################################################
# File Name: example.py
# Author:    Hanchen Jin
# Date:      Jun 9, 2018
#######################################################
# A simplified Python tutorial
# ----------------------------
# Please feel free to modify this scipt to explore 
# more interesting implementation in Python!
#######################################################
import time
import random

# 1. Hello world!
print("1. Hello world!")
print("Hello World!")

# 2. Data type
print("-----------------------------------------------------")
print("2. Data type")
a = 2018
b = 3.1415926
c = "DPE2018"
d = True
print("%d : %s; %f : %s; %s : %s; %s : %s;" % (a, type(a), b, type(b), c, type(c), str(d), type(d)))

# 3. Data structure
print("-----------------------------------------------------")
print("3. Data Structure")
l = [0,1,2,3,4,5]
d = {"Bob" : 20, "Alice" : 18}
t = ("Bob", 20, 3.1415926)
print("%s : %s; %s, %s; %s, %s;" % (str(l), type(l), str(d), type(d), str(t),type(t)))

# 4. Control flow
print("-----------------------------------------------------")
print("4. Control flow")
# if-elif-else
if l[0] == d["Bob"]:   # if 0 ?= 20
  print("Enter if.")
elif l[1] == d["Bob"]:
  print("Enter elif.")
else:
  print("Enter else.")
# for loop 
for i in t:  # loop through tuple t
  print(i),
print("")
# while loop
i = 0        # loop through list l
while (i < len(l)):
  print(l[i])
  i += 1
# 5. OOP
print("-----------------------------------------------------")
print("5. Objected-Oriented Programming")
# class for storing student information
class student_profile(object):
  # init class values
  def __init__(self, name, gender = "miss", age = "miss"):
    self.name   = name
    self.gender = gender
    self.age    = age 
  # print values when called like print(Bob)
  def __repr__(self):
    return "Name: %s; Gender: %s; Age: %s" % (self.name,self.gender,self.age)
  # calculate year of birth
  def year_birth(self):
    return "%s's year of birth: %d;" % (self.name, (2018 - int(self.age)))
# create new oblect called "Bob"
Bob = student_profile("Bob",age=20)
print(Bob)
print(Bob.age)
print(Bob.year_birth())
# 6. Sorting
# Selection Sort
def selectionSort(alist):
  """
  During each iteration of the inner-loop, selection sort places
  the smallest of the remaining unsorted elements at the end of 
  the sorted list.
  """
  for i in range(len(alist)):
    lowest = i
    for j in range(i, len(alist)):
        if(alist[lowest] > alist[j]):
            lowest = j
    temp = alist[i]
    alist[i] = alist[lowest]
    alist[lowest] = temp
#Comparison between Python's built-in sort function and selection sort
#Creating lists of size 100, 1000, and 10000
firstList = []
for i in range(100):
    firstList.append(random.randint(0, 101))
firstListCopy = firstList[:]
print("Unsorted firstList: ", firstList, "\n")

secondList = []
for i in range(1000):
    secondList.append(random.randint(0, 101))
secondListCopy = secondList[:]

thirdList = []
for i in range(10000):
    thirdList.append(random.randint(0, 101))
thirdListCopy = thirdList[:]

firstStartSS = time.time()
selectionSort(firstList)
firstEndSS = time.time()
print("Time for Selection Sort(Size 100): ", firstEndSS - firstStartSS, "\n")
secondStartSS = time.time()
selectionSort(secondList)
secondEndSS = time.time()
print("Time for Selection Sort(Size 1000): ", secondEndSS - secondStartSS, "\n")
thirdStartSS = time.time()
selectionSort(thirdList)
thirdEndSS = time.time()
print("Time for Selection Sort(Size 10000): ", thirdEndSS - thirdStartSS, "\n")
print("Sorted First List(using selection sort): ", firstList, "\n")

firstStartPS = time.time()
sorted(firstListCopy)
firstEndPS = time.time()
print("Time for Python Sorted Function(Size 100): ", firstEndPS - firstStartPS, "\n")
secondStartPS = time.time()
sorted(secondListCopy)
secondEndPS = time.time()
print("Time for Selection Sort(Size 1000): ", secondEndPS - secondStartPS, "\n")
thirdStartPS = time.time()
sorted(thirdListCopy)
thirdEndPS = time.time()
print("Time for Selection Sort(Size 10000): ", thirdEndPS - thirdStartPS, "\n")
print("Sorted First List(using sorted function): ", firstListCopy, "\n")
# 7. Recursion(Extension)
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21...
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2)
print("Fibonacci Sequence:", fib(1), ", ", fib(2), ", ", fib(3), ", ", fib(4), ", ", fib(5), ", ", fib(6), ", ", fib(7), "...")

