import numpy as np
import matplotlib as plt

##JENSEN
#test = np.random.exponential(1,size=10000)
#left = np.mean(np.log(test))
#right = np.log(np.mean(test))
#jensen = left < right

##LLN
#test = np.random.binomial(1, 1/2, 1000)
#average = []
#for i in range(0,len(test)):
#    tosum = test[0:i]
#    average.append(np.sum(tosum)/i)

## estimating pi using dots in a circle
#x = np.random.uniform(size=1000)
#y = np.random.uniform(size=1000)
#total = x**2+y**2
#pi = np.sum(total <1)*4

## visualization of CLT
#X = [] #matrix to hold all numbers
#for i in range(12):
#    xn = np.random.uniform(size=10000) #start with 
#    X.append(xn)
#Xbar = np.mean(X,axis=0)
#plt.pyplot.hist(Xbar)

#chi-squared - remember special case of the gamma
z = np.random.normal(size=10000)
z2 = z**2
x = np.random.chisquare(20, 10000)

#student ttest - remember effectively Z divided by chisquared
t= np.random.standard_t(10000,10000)

plt.pyplot.hist(z2)
plt.pyplot.hist(x)
plt.pyplot.hist(t)

