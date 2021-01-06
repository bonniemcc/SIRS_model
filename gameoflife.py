'''Game of Life class:
defines all useful functions for the model'''
import numpy as np

class GameOfLife:

    def __init__(self,n,method):
        self.n = n
        if method == 'random':
            self.state = self.randomconfig()
        if method == 'oscillator':
            self.state = self.oscillatorconfig()
        if method == 'glider':
            self.state = self.gliderconfig()

    def randomconfig(self):
        #generate n x n array of random 0s nd 1s
        state = np.random.randint(2,size=(self.n,self.n))
        return state 

    def oscillatorconfig(self):
        state = np.zeros([self.n,self.n])
        # choose random site in n x n matrix
        ni = np.random.randint(self.n)
        nj = np.random.randint(self.n)
        state[ni,nj] = 1
        state[ni+1,nj] = 1
        state[ni+2,nj] = 1
        return state 

    def gliderconfig(self):
        state = np.zeros([self.n,self.n])
        state[int(self.n/2),int(self.n/2)] = 1
        state[int(self.n/2),int(self.n/2)+1] = 1        
        state[int(self.n/2),int(self.n/2)+2] = 1 
        state[int(self.n/2)-1,int(self.n/2)+2] = 1      
        state[int(self.n/2)-2,int(self.n/2)+1] = 1                                                                                                                                                                                                                 
        return state 

    def test(self):
        #set up n x n matrix to store new configuration
        newstate = np.zeros([self.n,self.n])
        #loop through for one sweep
        for i in range(self.n):
            for j in range(self.n):
                # choose random site in n x n matrix
                #ni = np.random.randint(self.n)
                #nj = np.random.randint(self.n)
                #calculate sum of 8 surrounding neighbours
                s = self.neighbours(i,j)

                if self.state[i,j] == 1: #if cell is alive
                    if s > 3: # > 3 or < 2 live neighbours
                        newstate[i,j] = 0
                    if s < 2: # > 3 or < 2 live neighbours
                        newstate[i,j] = 0
                    if s ==2:
                        newstate[i,j] = 1
                    if s ==3:
                        newstate[i,j] = 1
                if self.state[i,j] == 0: #if cell is dead
                    if s == 3: #exactly 3 live neighbours
                        newstate[i,j] = 1
        self.state = np.copy(newstate)
        return np.count_nonzero(self.state==1) #number of infected sites


    #function returns sum of 8 neighbours
    def neighbours(self,i,j):
        a = self.state[(i+1)%self.n,j]
        b = self.state[(i-1)%self.n,j]
        l = self.state[i,(j-1)%self.n]
        r = self.state[i,(j+1)%self.n]
        a_r = self.state[(i+1)%self.n,(j+1)%self.n]
        a_l = self.state[(i+1)%self.n,(j-1)%self.n]
        b_r = self.state[(i-1)%self.n,(j+1)%self.n]
        b_l = self.state[(i-1)%self.n,(j-1)%self.n]
        n_sum = a + b + l + r + a_r + a_l + b_r + b_l
        return n_sum

    def centre_mass(self):
        result = np.where(self.state == 1)
        x_pos = result[1]
        y_pos = result[0]
        if max(x_pos)-min(x_pos)< 3 and max(y_pos)-min(y_pos)< 3:
            r_x = (np.sum(x_pos))/(len(x_pos))
            r_y = (np.sum(y_pos))/(len(y_pos))
            return [r_x,r_y]
        else:
            return [-1,-1]