import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sirs import SIRS

f = np.loadtxt('av_inf_frac.dat')
p1 = f[:,0]
p3 = f[:,1]
av = f[:,2]
v = f[:,3]


a = int(np.sqrt(len(av)))
matrix = np.reshape(av,(a,a))

p1u = np.unique(p1)
p3u = np.unique(p3)

X,Y = np.meshgrid(p1u,p3u)
fig, ax = plt.subplots(1,1)
cp = ax.contourf(X,Y,matrix)
cbar = fig.colorbar(cp)
plt.xlabel('p1')
plt.ylabel('p3')
plt.show()

plt.imshow(matrix, cmap='rainbow')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('p1')
plt.ylabel('p3')
plt.xticks([0,5,10,15,20],[0.0,0.25,0.50,0.75,1.0])
plt.yticks([0,5,10,15,20],[0.0,0.25,0.50,0.75,1.0])
plt.show()

matrix2 = np.reshape(v,(a,a))
X,Y = np.meshgrid(p1u,p3u)
fig, ax = plt.subplots(1,1)
cp = ax.contourf(X,Y,matrix2)
cbar = fig.colorbar(cp)
plt.xlabel('p1')
plt.ylabel('p3')
plt.show()

plt.imshow(matrix2, cmap='rainbow')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('p1')
plt.ylabel('p3')
plt.xticks([0,5,10,15,20],[0.0,0.25,0.50,0.75,1.0])
plt.yticks([0,5,10,15,20],[0.0,0.25,0.50,0.75,1.0])
plt.show()