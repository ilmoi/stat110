import numpy as np

#a = np.array([[1/3,1/3,1/3,0],[0,0,1/2,1/2],[0,1,0,0],[1/2,0,0,1/2]])
#b = a@a@a@a@a
#vals, vecs = np.linalg.eig(a)

#gamblers ruin
p = 1/2
sims = 100
N = 10

x = np.zeros(sims)
x[0]=5

for i in range(0,len(x)-1):
    if x[i] == 0:
        x[i+1] = 0
    elif x[i] == 10:
        x[i+1] = 10
    else:
        if np.random.binomial(1,p):
            x[i+1] = x[i]+1
        else:
            x[i+1] = x[i]-1