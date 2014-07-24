from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *
from matplotlib import rc
import ast
nitrans = np.genfromtxt('NiMnAlSiTransmission.csv', delimiter = ',', dtype =float)
niref = np.genfromtxt('NiMnAlSiReflection.csv', delimiter = ',', dtype =float)
nitrans_wavelength = [q[0] for q in nitrans]
nitrans_reading = [q[1] for q in nitrans]
niref_wavelength = [m[0] for m in niref]
niref_reading = [m[1] for m in niref]
absorption = np.zeros(len(niref_reading))
d = 243
i = 0
while(i<=len(niref_reading)-1):
	absorption[i] = -np.log((nitrans_reading[i])/(1-niref_reading[i]))
	i = i +1
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(nitrans_wavelength, absorption)
plt.title('Absorption Plot')
plt.xlabel(r'$ \lambda $ (nm)')
plt.ylabel(r'$ \alpha \  (nm^{-1}) $ ')
plt.show()

