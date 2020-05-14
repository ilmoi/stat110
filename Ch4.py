from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np

##matching problem simulation from Ch1, but this time we want to find the average
n = 100 #number of cards
repeats = 10**4 #how many times we want to repeat the experiment
ordered_nr = np.arange(n) #list of correctly ordered numbers
total_right = 0
right_vector = []
for i in range(repeats):
    random_nr = np.random.choice(n, n, replace = False) #our sample, WITHOUT REPLACEMENT!
    guessed_right = np.sum(ordered_nr==random_nr) #sum of guesses    
    right_vector.append(guessed_right)
prob = total_right/repeats
#comes out at 0.63, which is what we expected!
average = np.mean(right_vector)
#comes out as 1, exactly like we wanted!