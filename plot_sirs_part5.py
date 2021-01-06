import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gameoflife import GameOfLife

f = np.loadtxt('sirs_part5.dat')
f_im = f[:,0]
frac = f[:,1]
err = f[:,2]
#err = err/50

#plt.plot(f_im,frac)
plt.errorbar(f_im,frac,yerr = err)
plt.xlabel('Immune fraction')
plt.ylabel('Average infected fraction')
plt.title('Part 5: How the Immunity Fraction affcts the Infected Fraction')
plt.show()