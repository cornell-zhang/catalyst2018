#=============================================================
# Digit Recognition
#=============================================================
# Training data    : mnist (60000) + extra (312)
# Testing data     : drawing on canvas
# Image resolution : 28*28
# Prediction       : numbers from 0 to 9
#=============================================================
import time
import operator
import numpy

# K value
K = 10
# display training data
NUMBER = 7

# Class for Training image && Testing image
class Digit:
  # image data: label and pixels(data)
  def __init__(self):
    self.label = ''
    self.data  = []
    self.index = ''  # training image index from 1 to ...
  # build numpy array for pixels(data)
  def init(self):
    self.ndata = numpy.array(self.data)
  # calculate distance
  def distance(self,digit):
    return numpy.sum(abs(self.ndata - digit.ndata))
    """ extremely slow implementation
    dis = 0
    for i in range(len(self.ndata)):
      if self.ndata[i] != 0:
        dis += abs(self.ndata[i] - digit.ndata[i]) * WEIGHT
      else:
        dis += abs(self.ndata[i] - digit.ndata[i])
    return dis
    """

# digit recognition              
def digitrec(testing_data,training_set):
  final_res = 0
  #training_set = get_training_set()
  test = Digit()
  test.data = testing_data
  test.init()
  # start predicting
  results = []
  t1 = time.time()
  # calculate distance
  for train in training_set:
    """        
    if int(train.label) == NUMBER:
      for i in range(0,28):
        debug = []
        for j in range(0,28):
          debug.append(train.data[i*28+j])
        #print(debug)
      #print("+: "+str(train.label)+"==================================================================================")
    """
    #===== Implement your code here =====
    
    
    
    #print distance
    """    
    test_distance = 0
    for j in range(0,784):
      if train.data[j] != test.data[j]:
        test_distance += 1
    #print( "correct distance: %d; ",test_distance)
    """
    touple = distance, train
    results.append(touple)
  t2 = time.time()
  # sort distance
  #===== Implement your code here =====
  
  
  
  #print(results)
  t3 = time.time()
  labelmap = {}
  # KNN vote
  for y in range(0,K):
    #===== Implement your code here =====
    
    pass
    #print(result,result[1].label),
    #print("; training image index: %s" % result[1].index)
    
    
  print(labelmap)
  t4 = time.time()
  # sort vote
  #===== Implement your code here =====

  
  
  #print(labelmap)
  t5 = time.time()
  #print("distance:"+ str(t2-t1) + "; sort:" + str(t3-t2) + "; vote:" + str(t4-t3))
  #print(labelmap)
  # comment next line for test 
  final_res = int(labelmap[0][0])

  return final_res
