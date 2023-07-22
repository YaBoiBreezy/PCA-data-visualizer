#PCA data visualizer
#created by Alexander Breeze

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import random

def makePoint(numDim):
 p=[]
 for _ in range(numDim):
  p.append(random.uniform(0,1))
 return p

def makePointGauss(center,numDim):
 p=[]
 for d in range(numDim):
  p.append(random.gauss(center[d],0.1))
 return p

def makeFile(numCenters, numPoints, numDim):
 matrix=[]
 for _ in range(numCenters):
  center=makePoint(numDim)
  for _ in range(numPoints):
   matrix.append(makePointGauss(center,numDim))
 matrix=np.array(matrix)
 return matrix

def getFile(filename):
 matrix=[]
 f=open(filename, 'r') #if file not found, then fails here
 lines = f.readlines()
 for line in lines:
  matrix.append(list(map(float, line.rstrip().split(',')))) #separates line, converts all to int
 matrix=np.array(matrix) #if not all points have same dimensions, should fail here
 return matrix

def doPCA(matrix):
 if matrix.shape[1]>5: #do PCA on matrix
  pca=PCA(n_components=5)
  pca.fit(matrix)
  matrix=pca.transform(matrix)
 matrix=matrix-matrix.min(axis=0) #shift each column so minCol=0
 matrix=matrix / matrix.max(axis=0) #reduce each colMax to 1
 return matrix

def display(matrix):
 plt.scatter(x=matrix[:,0], y=matrix[:,1], c=matrix[:,2:])
 plt.show()
 return

def main():
 print("Welcome to the 5-dimensional scatterplot demo!")
 print("Please enter 3 space-separated ints for numCenters, numPoints (per center), and numDims, e.g. 4 10 5")
 print("Values must be >=1, >=1, >=5, respectively")
 print("OR")
 print("Make a file with data points similar to test1.txt and enter the path to it. Minimum 5 coordinates per point (aka per line)")
 inp=input()
 if ' ' in inp:
  inp=inp.split(' ')
  matrix=makeFile(int(inp[0]), int(inp[1]), int(inp[2]))
 else:
  matrix=getFile(inp)
 print(matrix)
 matrix=doPCA(matrix)
 print(matrix)
 display(matrix)

main()
