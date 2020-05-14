import numpy as np
import scipy
from scipy import stats
import matplotlib as plt

##Metropolis-hastings
#y = 3
#sigma = 1
#mu = 0
#tau = 2
#d = 1
#niter = 10000
#theta = np.zeros(niter)
#
#theta[0] = y #initialize theta at observed value y
#
#for i in range(1, niter):
#    theta_proposed = theta[i-1] + np.random.normal(loc=0, scale=d ,size=1)
##    print(theta_proposed)
#    
#    part1 = stats.norm.pdf(x=y, loc=theta_proposed, scale=sigma) * stats.norm.pdf(x=theta_proposed, loc=mu, scale=tau)
#    part2 = stats.norm.pdf(x=y, loc=theta[i-1], scale=sigma) * stats.norm.pdf(x=theta[i-1], loc=mu, scale=tau)
#    ratio = part1/part2
##    print(ratio)
#    
#    flip = np.random.binomial(n=1,p=min(ratio,1))    
#    if flip:
#        theta[i] = theta_proposed
#
#plt.pyplot.hist(theta[5000:])

#Gibbs
x = 7
labda = 10
a = 1
b = 1
niter = 10000
p = np.zeros(niter)
N = np.zeros(niter)

p[0] = 0.5
N[0] = 2*x

for i in range(1,niter):
    #we alternate between sampling p conditional on N and n conditional on p
    p[i] = np.random.beta(a=a+x, b=N[i-1]-x+b, size=1) #beta distribution, beta binomial conjugacy
    N[i] = x + np.random.poisson(lam = labda*(1-p[i-1]), size=1) #poisson(λp) distribution
    #as we sample better p > we estimat better Ns > as we estimate better Ns > we sample better ps > etc
    
plt.pyplot.hist(p[5000:])
#plt.pyplot.hist(N[5000:])
#charts look exactly like on page 554 of the book!