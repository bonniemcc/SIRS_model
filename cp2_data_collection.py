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
    '''fig = plt.figure()
    im=plt.imshow(a.state, animated=True, cmap = 'rainbow')
    plt.title("")'''
    

    eq_list = []

    for i in range(nsweeps):
        #perform flip/ swap spins
        a.test()
        '''plt.cla()
        im=plt.imshow(a.state, animated=True, cmap = 'rainbow', vmin=0,vmax=1)
        plt.title("")
        plt.draw()
        plt.pause(0.0001)'''
        if sys.argv[1] == 'r':
            eq_list.append(a.test())
            if len(eq_list) >= 4:
                if eq_list[-1] == eq_list[-2] == eq_list[-3] == eq_list[-4]:
                    with open("eq_time.dat", "ab") as f:
                        np.savetxt(f,[i-4])
                        break
        if sys.argv[1] == 'g':
            com = a.centre_mass()
            #np.savetxt('glider.txt',np.column_stack([com[0],com[1]]))
            if com[0] >0 and com[1]>0:
                with open("glider.dat", "ab") as f:
                    np.savetxt(f,np.column_stack([[i],com[0],com[1]]))

main()