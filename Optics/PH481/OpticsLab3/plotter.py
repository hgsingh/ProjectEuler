from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *

filename = 'scope.csv'

def getColumn(filename, column):
    with open(filename, newline = ' ') as csvfile:
        results = csv.reader(csvfile, delimiter="\t")
        return [result[column] for result in results]

'''
def getColumn(filename,column):
    with open(filename, newColumn = ' ') as csvfile:
        results = csv.reader(open(csvfile, delimiter="\t"))
        for result in results:
            return result[column]
'''
time = getColumn(filename,0)
volt = getColumn(filename,1)

plt.figure("Time/Volt")
plt.xlabel("Time(ms)")
plt.ylabel("Volt(mV)")
plt.plot(time,volt)