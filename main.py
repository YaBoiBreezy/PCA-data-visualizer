#PCA data visualizer
#created by Alexander Breeze

import sklearn
from sklearn import decomposition
import numpy as np

def get_file(filename):
 matrix=[]
 f=open(filename, 'r') #if file not found, then fails here
 lines = f.readlines()
 for line in lines:
  matrix.append(list(map(int, line.rstrip().split(',')))) #separates line, converts all to int
 matrix=np.array(matrix) #if not all points have same dimensions, should fail here
 return matrix

def doPCA(matrix):
 return

def display(matrix):
 return

def main():
 print("Welcome to the 5-dimensional scatterplot demo!")
 print("Please make a file with data points, following these rules:")
 print("Each line is one point, consisting of a comma separated list of coordinates")
 print("5 dimensions minimum per point, and each point must have the same number of dimensions")
 print("Then enter the path to the file and press enter, e.g. \"./test1.txt\"")
 filename=input()
 print("Opening file")
 matrix=get_file(filename)
 print(matrix)

main()