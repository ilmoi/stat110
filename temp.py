from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np

test = np.random.geometric(0.5, 100000)
payoff = test*2
av = np.average(payoff)