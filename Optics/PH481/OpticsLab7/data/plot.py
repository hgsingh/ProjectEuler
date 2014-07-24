from __future__ import division 
import matplotlib.pyplot as plt
import numpy as np
import csv
from sys  import *
from io import *
from matplotlib import rc
import ast

A  = np.genfromtxt('OrangeTrans.csv',delimiter = ',', dtype = float)
red = np.genfromtxt('RedTrans.csv', delimiter =',', dtype = float)
green = np.genfromtxt('greenTrans.csv',delimiter=',', dtype = float)
heneR = np.genfromtxt('HeNeRef.csv',delimiter=',', dtype = float)
heneT = np.genfromtxt('HeNeTrans.csv', delimiter = ',', dtype =float)
niref = np.genfromtxt('NiMnAlSiReflection.csv', delimiter = ',', dtype =float)
nirefFit = np.genfromtxt('NiMnAlSiReflectionFit.csv', delimiter = ',', dtype =float)
nirefrac = np.genfromtxt('NiMnAlSiRefraction.csv', delimiter = ',', dtype =float)
nitrans = np.genfromtxt('NiMnAlSiTransmission.csv', delimiter = ',', dtype =float)
nirefrac_wavelength = [p[0] for p in nirefrac]
nirefrac_reading= [p[1] for p in nirefrac]
nitrans_wavelength = [q[0] for q in nitrans]
nitrans_reading = [q[1] for q in nitrans]
niref_wavelength = [m[0] for m in niref]
niref_reading = [m[1] for m in niref]
nirefFit_wavelength = [n[0] for n in nirefFit] 
nirefFit_reading = [n[1] for n in nirefFit]
A_wavelength = [i[0] for i in A]
A_reading = [i[1] for i in A]
red_wavelength = [j[0] for j in red]
red_reading = [j[1] for j in red]
green_wavelength = [k[0] for k in green]
green_reading = [k[1] for k in green]
heneR_wavelength = [l[0] for l in heneR]
heneT_wavelength = [h[0] for h in heneT]
heneR_reading = [l[1] for l in heneR]
heneT_reading = [h[1] for h in heneT]
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
p1,= ax.plot(nirefrac_wavelength, nirefrac_reading,'.')
p2, = ax.plot(nitrans_wavelength, nitrans_reading,'-')
plt.title('NiMnAlSi Refraction and Transmission')
plt.xlabel(r'$ \lambda $ (nm)')
plt.ylabel('I')
plt.legend([p1, p2], [" Refraction", "Transmission"], loc = 'best')
plt.show()


