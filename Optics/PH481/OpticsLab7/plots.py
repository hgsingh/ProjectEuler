from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *
from matplotlib import rc
import ast

#plotting for m vs x
v_out = [.00407 , .0453 , .0636, .258, .580,.871,1.1598,1.41,1.60,1.68,1.65,1.51,1.31,.994,.680,.383,.157,.133,.100]
theta = np.arange(110,300,10)
func1 = np.max(v_out)*((np.cos(theta*(np.pi/180)))**2)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
p1, = ax.plot(theta, v_out,'o')
p2, = ax.plot(theta, func1)
plt.title('Experimental Verification of Law of Malus')
plt.xlabel(r'$ \theta $')
plt.ylabel('V_{out} (V)')
plt.legend([p1, p2], [" Experimental", "Theoretical"], loc = 'best')
plt.show()


