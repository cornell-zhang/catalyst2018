import sqlite3
import json
import os
import sys
from read_image import get_images
from digitrec import digitrec

# number of training images (2000) and testing images (100)
# accuracy under this configuration: 91%
TRAIN_IMAGE = 2000
TEST_IMAGE  = 100

# running script
if __name__ == '__main__':
  print("Lab3: Digit Recognition")
  print("Reading training image and testing image..."),
  # training image : first 10 values
  # testing image  : last value
  dataset = get_images(TRAIN_IMAGE, TEST_IMAGE) 
  testing_set   = dataset[TRAIN_IMAGE:(TRAIN_IMAGE + TEST_IMAGE)]
  training_set  = dataset[0:TRAIN_IMAGE]
  print("Done!")
  print("Total number of training images : %d;" % len(training_set))
  print("Total number of testing images : %d;" % len(testing_set))
  print("Start prediction...")
  value = []
  for i in range(TEST_IMAGE):
    value.append(digitrec(testing_set[i].data, training_set))
  print("Checking final result...")
  #print(value)
  counter = 0
  for i in range(TEST_IMAGE):
    if value[i] == int(testing_set[i].label):
      counter += 1
  accuracy = float(counter) / float(TEST_IMAGE) * 100  
  print("Accuracy: %.1f %%" % accuracy)
  print("Script END.")