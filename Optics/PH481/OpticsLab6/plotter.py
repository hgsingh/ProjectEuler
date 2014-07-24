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
'''
A  = np.genfromtxt('rectangle1.csv', dtype = float)
B = np.genfromtxt('rectangle2.csv', dtype = float)
E = np.genfromtxt('6acircularvalue.csv', dtype = float)
print B
'''
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
'''
'''
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

pixel = np.arange(0,640)
distance = np.zeros_like(A)
for j in range(len(pixel)-1):
	distance[j] = pixel[j]*(0.43/640)
'''
#plotting for m vs x
x_pos = [32.9 , 21.15 , 16.75, 13.85 , 11.65]
m = [1,1/2,1/3,1/4,1/5] 
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(m, x_pos,'-o')
plt.xlabel(r'$ \frac{1}{n} $')
plt.ylabel('x postion (cm)')
plt.show()


