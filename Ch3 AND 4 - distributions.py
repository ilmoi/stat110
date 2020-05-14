from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np
import matplotlib as plt

#CHAPTER 3
#BINOMIAL/BERNOULLI - returns number of successes in a fixed number of trials
#simulate 1000 tests of 10 fair coinflips
n = 10 #fixed number of trials. if you make this 1, becomes bernoulli
p = 0.5 #probability of success on each
repeats = 1000 #how many times re-run the experiment
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

#HYPERGEOMETRIC
#aces in a 5-hand poker hand
w = 4
b = 48
n = 5
repeats = 100000
test = np.random.hypergeometric(w,b,n,repeats)
#result = np.sum(test==1)/(repeats)
#plt.pyplot.hist(test)

#DISCRETE
test = np.random.uniform(-1,0,repeats)
#plt.pyplot.hist(test)

#CHAPTER 4
#NEGATIVE BINOMIAL - returns number of failures until the fixed number of successes reached
n = 10 #fixed number of successes to reach (if you make this 1 = becomes geometric)
p = 0.5 #probability of success
repeats = 1000 #how many times re-run the experiment
test = np.random.binomial(n,p, repeats) 
result = np.sum(test)/(n*repeats)
#plt.pyplot.hist(test)

#POISSON
lam = 1 #lambda or "rate"
repeats = 1000 #how many times re-run the experiment
test = np.random.poisson(lam, repeats) 
result = np.sum(test)/(n*repeats)
plt.pyplot.hist(test)