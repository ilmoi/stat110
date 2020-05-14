from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np
import matplotlib as plt

#simulate 1000 tests of 10 fair coinflips
n = 10
p = 0.5
repeats = 1000
test = np.random.binomial(n,p, repeats) 
result = np.sum(test)/(n*repeats)

# simulate 1000 tests of 20 patients taking a treatment with 60% success
n = 20
p = 0.6
repeats = 1000
test = np.random.binomial(n, p, repeats)
result = np.sum(test)/(n*repeats)

#how often will we get exactly 2 heads on a fair coin flip
n = 2
p = 0.5
repeats = 1000
test = np.random.binomial(n, p, repeats)
result = np.sum(test==2)/(n*repeats)
#plt.pyplot.hist(test)

#aces in a 5-hand poker hand
w = 48
b = 48
n = 10
repeats = 100000
test = np.random.hypergeometric(w,b,n,repeats)
#result = np.sum(test==1)/(repeats)
plt.pyplot.hist(test)

##test discrete
#test = np.random.uniform(-1,0,repeats)
#plt.pyplot.hist(test)

