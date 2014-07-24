from __future__ import division
import numpy as np
import matplotlib.pylab as p;
import matplotlib.pyplot as plt
from matplotlib import rc


b = np.linspace(-10, 10, 1000)
I= 4*(np.sinc(b))**2
S = 4*((np.sinc(b))**2)*(np.cos(3*b))**2
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(b,I)
ax.plot(b,S)
plt.xlabel(r'$\beta$')
plt.ylabel('I')
plt.savefig('pattern.png')
plt.close(fig)

