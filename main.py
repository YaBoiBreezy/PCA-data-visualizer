#PCA data visualizer
#created by Alexander Breeze

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def get_file(filename):
 matrix=[]
 f=open(filename, 'r') #if file not found, then fails here
 lines = f.readlines()
 for line in lines:
  matrix.append(list(map(float, line.rstrip().split(',')))) #separates line, converts all to int
 matrix=np.array(matrix) #if not all points have same dimensions, should fail here
 return matrix

def doPCA(matrix):
 pca=PCA(n_components=5)
 pca.fit(matrix)
 matrix=pca.transform(matrix) #do PCA on matrix
 matrix=matrix-matrix.min(axis=0) #shift each column so minCol=0
 matrix=matrix / matrix.max(axis=0) #reduce each colMax to 1
 return matrix

def display(matrix):
 plt.scatter(x=matrix[:,0], y=matrix[:,1], c=matrix[:,2:])
 plt.show()
 return

def main():
 print("Welcome to the 5-dimensional scatterplot demo!")
 print("Please make a file with data points, following these rules:")
 print("Each line is one point, consisting of a comma separated list of coordinates")
 print("5 dimensions minimum per point, and each point must have the same number of dimensions")
 print("Then enter the path to the file and press enter, or use the builtin demo \"./test1.txt\"")
 #filename=input()
 filename="./test1.txt"
 print("Opening file")
 matrix=get_file(filename)
 print(matrix)
 matrix=doPCA(matrix)
 print(matrix)
 display(matrix)

main()