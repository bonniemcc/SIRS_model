'''Checkpoint 2: SIRS'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sirs import SIRS

def main():

    if len(sys.argv) != 7:
        print('User input: python cp2.py n #sweeps p1 p2 p3 immunity:y/n?')
        quit()

    #user inputs lattice size, # of sweeps
    n = int(sys.argv[1])
    nsweeps = int(sys.argv[2]) 
    p1 = sys.argv[3] 
    p2 = sys.argv[4] 
    p3 = sys.argv[5]
    Im = sys.argv[6]

    f=0.1
    a = SIRS(n)
    if Im == 'y':
        a.immune(f)

    #set up animation (pass lattice to plot)
    fig = plt.figure()
    im=plt.imshow(a.state, animated=True, cmap = 'rainbow')
    plt.title("")

    for i in range(nsweeps):
        a.test(p1,p2,p3)
        plt.cla()
        im=plt.imshow(a.state, animated=True, cmap = 'rainbow', vmin=-1,vmax=2)
        plt.title("")
        plt.draw()
        plt.pause(0.0001)

main()