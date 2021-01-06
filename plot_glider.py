import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gameoflife import GameOfLife

f = np.loadtxt('glider.dat')
t = f[:,0]
x = f[:,1]
y = f[:,2]

time = np.linspace(0,len(x),len(x))

plt.scatter(t,x,s=10)
plt.scatter(t,y,s=10)
plt.ylabel('centre of mass position (lattice index)')
plt.xlabel('time/ number of sweeps')
plt.legend(['x','y'])
plt.show()

#Find speed
#use sweeps ~515 to ~640
t2 = t[515:640]
x2 = x[515:640]
y2 = y[515:640]

(a,b) = np.polyfit(t2, x2, 1)
(c,d) = np.polyfit(t2, y2, 1)

print('x velocity: ',a)
print('y velocity: ',c)

speed = np.sqrt(a**2 + c**2)
print('speed of glider: ',speed)