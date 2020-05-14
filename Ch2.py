from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np

# simulate monty-hall
runs = 1000
strategy = ['switch','stay'][0]

count = 0
for i in range(runs):
    car = np.random.choice(3,1)+1
    guess = 1
    if strategy == 'stay':
        if guess == car:
            count+=1
    else:
        if car == 2 or car == 3:
            count+=1

success = count/runs