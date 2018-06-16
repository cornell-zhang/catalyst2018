#=============================================================
# Digit Recognition - Part 1
#=============================================================
# Training data    : mnist (10) 
# Testing data     : mnist (1)
# Image resolution : 28*28
# Prediction       : numbers from 0 to 9
#=============================================================
import time
import operator
import numpy
import check_result

# K value
K = 10
# display training data
NUMBER = 7

# Class for Training image && Testing image
class Digit:
  # image data: label and pixels(data)
  def __init__(self):
    self.label = '' #The number that corresponds to this digit image
    self.data  = [] #List storing the pixels corresponding to the hand-written digit
    self.index = ''  # training image index from 1 to ...
  # build numpy array for pixels(data)
  def init(self):
    self.ndata = numpy.array(self.data)
  # calculate distance
  def distance(self,digit):
    return numpy.sum(abs(self.ndata - digit.ndata))
    """ correct implementaion but runs slowly
    dis = 0
    for i in range(len(self.ndata)):
      if self.ndata[i] != 0:
        dis += abs(self.ndata[i] - digit.ndata[i]) * WEIGHT
      else:
        dis += abs(self.ndata[i] - digit.ndata[i])
    return dis
    """

# Digit Recognition              
def digitrec(testing_data,training_set):
  """
  Function that returns the predicted digit drawn in testing_data.
  
  The testing_data argument contains the 2D array filled with 
  0's and 1's, which represents the hand-written digit.
  
  The training_set argument is a list of Digit objects, which
  the function will use to compare against the testing image.
  """
  #training_set = get_training_set()
  
  #creating a new object of class Digit
  #and filling in its data members with the appropriate values
  test = Digit() 
  test.data = testing_data
  test.init()
  # start predicting
  results = [] #list that stores tuples of distances(from testing image to training image), and the Digit object associated with the training image
  t1 = time.time()
  prediction = [] 
  temp_dis   = [] 
  temp_s_dis = []
  temp_s_idx = []
  # -------------------------------------------------------------------
  # 1.calculate distance
  # -------------------------------------------------------------------
  """
  Input: Training images, testing image
  Ouput: list of distances to each of the training images 
      Example: [19103,46569,11471,52763,29693,7225,11152,29767,23770,16454]
  """
  print("Calculating distances...")
  #print(test.data)
  #print(training_set[0].data)
  for train in training_set:
    """        
    if int(train.label) == NUMBER:
      for i in range(0,28):
        debug = []
        for j in range(0,28):
          debug.append(train.data[i*28+j])
        print(debug)
      print("+: "+str(train.label)+"==================================================================================")
    """
    #===== Implement your code here =====
    #Calculate individual distances here
    
    
    
    #print distance
    """    
    test_distance = 0
    for j in range(0,784):
      if train.data[j] != test.data[j]:
        test_distance += 1
    print( "correct distance: %d; ",test_distance)
    """
    #Append tuples of the distance to this training image,
    #along with its Digit object, to the list, results.
    temp_dis.append(distance)
    touple = distance, train
    results.append(touple)
  # store distances for checking
  prediction.append(temp_dis)
  t2 = time.time()
  # -------------------------------------------------------------------
  # 2.sort distances
  # -------------------------------------------------------------------
  """
  Input:  results
  Output: sorted results according to distance
  """
  print("Start sorting distance...")
  #===== Implement your code here =====
  #Use built-in sort function.
  
  #===== EXTENSION BEGIN =====
  def adaptiveMergeSort(L):
      """
      This function sorts a list by distance.
      
      L is the list of tuples that you would like to sort by distance
      """
      #Base Case()
      #How small a list, where the sort becomes trivial?
      #Replace "condition" with your own condition
      if(condition):
          pass
      #Split the list into two halves
      firstList = []
      #Implement your code here
      #Append all even-indexed elements to this first list.
      secondList = []
      #Implement your code here
      #Append all odd-indexed elements to this second list.
      
      #Use helper functions below to check whether the two lists are already sorted
      #Replace "condition" with your own contition
      if(condition):
          pass #Use the other helper function to help you merge the two lists
      #Otherwise, the two lists aren't sorted
      else:
          #Fill this section with recursive calls
          #Once you have sorted each half, what must you do to combine them into one full sorted list?
          pass #Return the entire sorted list
  
  def tryMerge(firstList, secondList):
      """
      This function returns a boolean that tells whether both lists are sorted.
      
      The lists, firstList and secondList, are the ones that must be checked.
      """
      #Iterate through each list, checking whether it's in order.
      #Hint: You will need two loops, and the instant anything is out of order, you may return False.
      pass
  
  def merge(firstList, secondList):
      """
      This function merges two sorted lists into a single sorted list, which it will return.
      
      The arguments, firstList and secondList, are both sorted lists.
      """
      #Initializing a list that will store the values in order.
      sortedList = []
      #Use loops to iterate through each of the lists, picking the smaller of the two elements to place in the sorted list.
      #Hint: You will need two pointers(one for each list). Be mindful of your variables, and when you should increment them!
      pass
  #===== EXTENSION END =====
  
  #print(results)
  t3 = time.time()
  # store sorted distance for checking
  for item in results:
    temp_s_dis.append(item[0])
    temp_s_idx.append(item[1].index)
  prediction.append(temp_s_dis)     # distances
  prediction.append(temp_s_idx)     # corresponding index
  # -------------------------------------------------------------------
  # 3.knn vote
  # -------------------------------------------------------------------
  """
  Input:  sorted results
  Output: labelmap
  """
  print("Start knn vote...")
  #Initialize labelmap...
  #Keys will be the Digit labels, and values wil be quantity
  labelmap = {}
  #Iterate through the K-nearest neighbors, placing their labels and quantity in the labelmap
  #Hint: There should be two different cases: one for when the label already exists in the map,
  #and one for when it doesn't.
  for y in range(0,K):
  #===== Implement your code here =====
    
    pass
    #print(result,result[1].label),
    #print("; training image index: %s" % result[1].index)
    
    
  print(labelmap)
  # store labelmap for checking
  prediction.append(labelmap)
  t4 = time.time()
  # -------------------------------------------------------------------
  # 4.sort vote
  # -------------------------------------------------------------------
  """
  Input:  labelmap
  Output: sorted labelmap
  """
  print("Start sorting vote...")
  #Hint: Python has a built in function to help you do this.
  #===== Implement your code here =====

  
  
  #print(labelmap)
  # store sorted labelmap for checking
  prediction.append(labelmap)
  t5 = time.time()
  # -------------------------------------------------------------------
  # 5.check result
  # -------------------------------------------------------------------
  check_result(prediction)
  # print runtime
  #print("distance:"+ str(t2-t1) + "; sort:" + str(t3-t2) + "; vote:" + str(t4-t3))
  # print(labelmap)
  # return result
  final_res = int(labelmap[0][0])

  return final_res
