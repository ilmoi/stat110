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

#HYPERGEOMETRIC
#aces in a 5-hand poker hand
w = 4
b = 48
n = 5
repeats = 100000
test = np.random.hypergeometric(w,b,n,repeats)
result = np.sum(test==1)/(repeats)

#DISCRETE UNIFORM - note upper bound is EXclusive
test = np.random.randint(-1,1,repeats)

#CHAPTER 4
#NEGATIVE BINOMIAL - returns number of failures until the fixed number of successes reached
n = 10 #fixed number of successes to reach (if you make this 1 = becomes geometric)
p = 0.5 #probability of success
repeats = 1000 #how many times re-run the experiment
test = np.random.binomial(n,p, repeats) 
result = np.sum(test)/(n*repeats)

#POISSON
lam = 1 #lambda or "rate" - eg 1 event per hour
repeats = 1000 #how many times re-run the experiment
test = np.random.poisson(lam, repeats) #tells us how many events per hours happened
avg = np.sum(test)/(repeats) #average probability of happening, which is equal to lambda, like we expected

#CHAPTER 5
#UNIFORM - note this is by default continuous, not discrete. Discrete is done through randint
test = np.random.uniform(-1,0,repeats)

#NORMAL
repeats = 10000
test = np.random.normal(size=repeats) 
#two ways to get to the same normal dist
mu = 4
sigma = 2
#1
test = np.random.normal(mu,sigma,size=repeats) 
#2
test = mu + sigma*np.random.normal(size=repeats)

#EXPO
repeats = 10000
test = np.random.exponential(size=repeats) 

#testing uniforsality of the uniform
u = np.random.uniform(-1,0,repeats)
x = np.log(test/(1-test))
test = x

#POISSON PROCESS
#EXPO
repeats = 10000
lambda_rate = 1/2 #1 success every 2 hours
expo = np.random.exponential(scale = lambda_rate, size=repeats) # each number tells me how long I waited until 1 success, in hours
t = np.cumsum(expo)[-1] #this is the total waiting time for 10k successes, in hours
avg = t/repeats #as expected, this gives us the same as lambda

#BETA
repeats = 10000
test = np.random.beta(a=40,b=40,size=repeats) 

#PLOTTING
plt.pyplot.hist(test)