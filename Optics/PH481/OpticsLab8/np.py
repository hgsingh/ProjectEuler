from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *
from matplotlib import rc
import ast

#plotting for m vs x
d = 1.5
alpha = 66.5
v_out = [1, (1*(75/80)),(1*(75/85)),(1*(75/100))]
t = [abs(216-360),abs(217-360),abs(218-360),abs(221-360)]
c = np.linspace(1,.7,10)
func1 = d*c*alpha
A = np.vstack([t, np.ones(len(t))]).T
m, co = np.linalg.lstsq(A, v_out)[0]
print m,co
print m/d

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
p1, = ax.plot(v_out, t, 'o')
p2, = ax.plot(c, func1)
plt.title('Experimental Verification of Measured Rotation')
plt.xlabel(r'$ concentration $')
plt.ylabel(r'$\beta$')
plt.legend([p1, p2], [" Experimental (633 nm)", "Theoretical (589 nm)"], loc = 'best')
plt.show()


