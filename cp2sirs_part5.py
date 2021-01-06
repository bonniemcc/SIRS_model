'''Checkpoint 2: SIRS'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sirs import SIRS
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from scipy.stats import sem

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

    #a = SIRS(n)

    p1 = 0.5
    p2 = 0.5
    p3 =0.5
    f_list = np.linspace(0,1,101)
    means = []
    errors = []

    fracs = np.zeros((len(f_list),5))

    for k in range(5): #repeat 5 times

        print(k)

        for m in range(len(f_list)):

            f = f_list[m]
            a = SIRS(n)
            a.immune(f)
            inf_frac = []

            for i in range(nsweeps):
                inf = a.test(p1,p2,p3)/(n*n)
                if i>100:  
                    inf_frac.append(inf)
                    if inf == 0:
                        break
            if inf == 0:
                av_if = 0
                #err_if = 0
            else:
                av_if = np.mean(inf_frac)
                #err_if = sem(inf_frac)
            fracs[m,k] = av_if

            print(inf_frac)
            print(av_if)
    
    for l in range(len(f_list)):
        mean = np.mean(fracs[l])
        error = sem(fracs[l])
        means.append(mean)
        errors.append(error)

    #np.savetxt('sirs_part5.dat',np.column_stack([f_list,means,errors]))


main()