'''SIRS class:
defines all useful functions for the model'''
import numpy as np

class SIRS:

    def __init__(self,n):
        self.n = n
        #generate n x n array of random 1s, 0s and -1s
        self.state = np.random.randint(3,size=(self.n,self.n)) -1

    def test(self,p1,p2,p3):
        for l in range(self.n*self.n):
            # choose random site in n x n matrix
            i = np.random.randint(self.n)
            j = np.random.randint(self.n)

            if self.state[i,j] == -1: #if cell is susceptible
                if self.neighbour_check(i,j) == True:
                    if np.random.rand() < float(p1):
                        self.state[i,j] = 1
            elif self.state[i,j] == 1: #if cell is infected
                if np.random.rand() < float(p2):
                    self.state[i,j] = 0
            elif self.state[i,j] == 0: #if cell is recovered
                if np.random.rand() < float(p3):
                    self.state[i,j] = -1
        return np.count_nonzero(self.state==1) #number of infected sites
        

    def neighbour_check(self,i,j):
        a = self.state[(i+1)%self.n,j]
        b = self.state[(i-1)%self.n,j]
        l = self.state[i,(j-1)%self.n]
        r = self.state[i,(j+1)%self.n]
        if a == 1 or b == 1 or l ==1 or r ==1:
            return True
        else: 
            return False

    def immune(self,f):
        nf = (1-f)/3
        self.state = np.random.choice(4, size=(self.n,self.n), p = [nf,nf,nf,f]) -1