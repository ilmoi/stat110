from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np
import scipy as sp
from scipy import integrate #you need to import this next to scipy itself, weird but works
from scipy import stats #you need to import this next to scipy itself, weird but works
import matplotlib as plt

#CONTINUOUS
#we can find any moment by doing LOTUS and normal integration
#eg lets find the 6th moment of Z
test6 = sp.integrate.quad(lambda x: x**6 * sp.stats.norm.pdf(x), np.NINF, np.PINF)

#3rd return 0 (odd moment of a symmetric function) as expected
test3 = sp.integrate.quad(lambda x: x**3 * sp.stats.norm.pdf(x), np.NINF, np.PINF)

#4th return 3 (kurtosis+3) as expected
test4 = sp.integrate.quad(lambda x: x**4 * sp.stats.norm.pdf(x), np.NINF, np.PINF)

#DISCRETE
result = np.array([x**2*sp.stats.poisson.pmf(x,mu=7) for x in range(0,1000)]).sum()
#(!!!!!!) when integrating we want to use infinity as upper limit, but in summation we can't -as it will go into an infinite loop

#note that scipy also comes with prebuilt in frunctions for mean, variance, skew, kurtosis
mean, var, skew, kurt = stats.poisson.stats(mu=7, moments='mvsk')