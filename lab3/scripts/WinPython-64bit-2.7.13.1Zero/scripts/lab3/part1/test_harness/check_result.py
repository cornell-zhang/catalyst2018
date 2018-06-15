#====================================================================
# Test Harness
#====================================================================
import csv
import sys

# loading result
def load_result():
  res = []
  print("Start reading correct results..."),
  with open('data/result.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    # count number of rows in CSV file
    row_numebr = 0
    for row in csvreader:
      res_temp = []
      for col in row:
        res_temp.append(col)
      res.append(res_temp)
    print("Done!")
  return res

def test_fail(res,pre):
  print("Wrong!")
  print("Correct result: "),
  print(res)
  print("Your result: "),
  print(pre)
  sys.exit("Quit script.") 
  
def check_result(pre):
  res = load_result()
  #print(pre)
  #print(res)
  print("Checking distances..."),
  for i in range(len(res[0])):
    if int(res[0][i]) != pre[0][i]:
      test_fail(res[0],pre[0])
  print("PASSED!")
  print("Checking the sorting result of distances and corresponding indexes..."),
  for i in range(len(res[1])):
    if int(res[1][i]) != pre[1][i] and int(res[2][i]) != pre[2][i]:
      test_fail(res[1],pre[1])
  print("PASSED!")
  print("Checking knn vote..."),
  if pre[3][res[3][0]] != int(res[3][1]):
    test_fail(res[3],pre[3])
  if pre[3][res[3][2]] != int(res[3][3]):
    test_fail(res[3],pre[3])
  if pre[3][res[3][4]] != int(res[3][5]):
    test_fail(res[3],pre[3])
  print("PASSED!")
  print("Checking the sorting result of KNN vote..."),
  for i in range(len(res[3])):
    if int(res[3][i]) != int(pre[4][i/2][i%2]):
      test_fail(res[3],pre[4])
  print("PASSED!")


