import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gameoflife import GameOfLife

f = np.loadtxt('sirs3.dat')
p1 = f[:,0]
#av = f[:,1]
v = f[:,1]
err = f[:,2]
#err = err/(2500*50)

#plt.plot(p1,v)
plt.errorbar(p1,v,yerr = err)
plt.xlabel('p1')
plt.ylabel('variance')
plt.title('Variance vs. p1 for p2=p3=0.5')
plt.show()
