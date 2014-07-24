from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *
from matplotlib import rc
import ast
'''
filename = 'rectangle1.csv'
filename1 = 'rectangle2.csv'

'''
def arr1(filename, column):
	array1 = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for column in reader:
			array1.append(column)
	return array1
def arr2(filename, column):
	array2 = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for column in reader:
			array2.append(column)
	return array2
I = arr1(filename, 0)
I2 = arr2(filename1,0)
A = np.reshape(I,len(I))
B = np.reshape(I2, len(I2))
C = np.zeros_like(A)
D = np.zeros_like(B)
for i in range(len(A)-1):
	C[i] = ast.literal_eval(A[i])
for k in range(len(B)-1):
	D[k] = ast.literal_eval(B[k])
print C, D

#find max then plot
A_max = np.amax(A)
B_max = np.amax(B)
print B_max
E_max = np.amax(E)
C = np.zeros(len(A))
D = np.zeros(len(B))
F = np.zeros(len(E))
for i in range(len(A)-1):
	C[i] = A[i]/A_max
for k in range(len(B)-1):
	D[k] = B[k]/B_max
for l in range(len(E)-1):
	F[l] = E[l]/E_max
