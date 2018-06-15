#============================================================
# Lab3: Digit recognization
#============================================================
# Training image : mnist (60000) + extra (312)
# Testing image  : drawing on canvas
# Prediction     : numbers from 0 to 9
#============================================================
import sqlite3
import json
import os
import sys
from read_image import get_images
from digitrec import digitrec

# 3 "0", 5 "1", 2 "2"
TRAIN_IMAGE = 10
# "1"
TEST_IMAGE  = 1

# running script
if __name__ == '__main__':
  print("Lab3: Digit Recognition")
  print("Reading training image and testing image...")
  # training iamge : first 10 values
  # testing image  : last value
  dataset = get_images()
  testing_data  = dataset[-1].data
  testing_label = dataset[-1].label
  training_set  = dataset[:-1]
  print("Start prediction...")
  value = digitrec(testing_data, training_set)
  print("Checking final result..."),
  if value == int(testing_label):
    print("Test PASSED!")
  else:
    print("Test FAILED...")
  print("Script END.")
