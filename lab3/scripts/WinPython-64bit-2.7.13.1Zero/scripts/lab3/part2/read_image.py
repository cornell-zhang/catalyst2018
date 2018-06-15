#====================================================================
# loading training images
#====================================================================
# Input:  csv file of mnist
# Output: images and label in the class Digit
#====================================================================
import csv
from digitrec import Digit

# shifting offeset
SHIFT_OFFSET = 4 # row 4
ROW_SIZE = 28

# load training data
def get_images(TRAIN_IMAGE, TEST_IMAGE):
  dataset = []
  with open('data/mnist_data.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    row_number = 0
    # one image per row
    for row in csvreader:
      # ignore first row - pixel index
      if not row_number == 0:
        data = Digit()
        dataset.append(data)
        data.index = row_number
        col_number = 0
        # shift counter
        s_counter = 0
        flag = 1
        for col in row:
          pixels = []
          # first value - label
          if col_number == 0:
            data.label = col
          # 28*28 pixels
          else:
            data.data.append(int(col))
          col_number = col_number + 1
        data.init()
      # count number of rows
      row_number = row_number + 1
      # stop when loading enough images
      if (row_number == (TRAIN_IMAGE + TEST_IMAGE + 1)):
        break
    #print(row_number-1)
  return dataset
