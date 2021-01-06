'''Checkpoint 2: the game of life'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gameoflife import GameOfLife

def main():

    if len(sys.argv) != 4:
        print('User input: python cp2.py initial_config(r,o,g) n #sweeps')
        quit()

    #user inputs lattice size, # of sweeps
    n = int(sys.argv[2])
    nsweeps = int(sys.argv[3]) 
    
    if sys.argv[1] == 'r':
        a = GameOfLife(n,'random')

    elif sys.argv[1] == 'o':
        a = GameOfLife(n,'oscillator')

    elif sys.argv[1] == 'g':
        a = GameOfLife(n,'glider')

    else:
        print('User input: python cp2.py initial_config(r,o,g) n #sweeps')

    #set up animation (pass lattice to plot)
    fig = plt.figure()
    im=plt.imshow(a.state, animated=True, cmap = 'rainbow')
    plt.title("")

    for i in range(nsweeps):
        #perform flip/ swap spins
        a.test()
        plt.cla()
        im=plt.imshow(a.state, animated=True, cmap = 'rainbow', vmin=0,vmax=1)
        plt.title("")
        plt.draw()
        plt.pause(0.0001)

main()