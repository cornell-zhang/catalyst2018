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

