import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gameoflife import GameOfLife

f = np.loadtxt('eq_time.dat')
#eq_time = f[:,0]

plt.hist(f, 50)#bins='auto')
plt.ylabel('frequency')
plt.xlabel('time/ number of sweeps')
plt.show()
