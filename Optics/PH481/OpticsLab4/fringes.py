from __future__ import division
import numpy as np
import matplotlib.pylab as p;
import matplotlib.pyplot as plt
from matplotlib import rc

F = 5.34
k  = 2*np.pi/578*10**-9
d = 0.0065561
#theta = np.linspace(0,2*np.pi,100)
delta =  np.linspace(0,15,100)
I = (1 + (F*((np.sin(delta))**2)))**-1
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(delta,I)
plt.savefig('fringes.png')
plt.close(fig)
#end relaxation
