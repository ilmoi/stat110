from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np

##matching problem simulation
#n = 100 #number of cards
#repeats = 10**4 #how many times we want to repeat the experiment
#ordered_nr = np.arange(n) #list of correctly ordered numbers
#total_right = 0
#for i in range(repeats):
#    random_nr = np.random.choice(n, n, replace = False) #our sample, WITHOUT REPLACEMENT!
#    guessed_right = np.sum(ordered_nr==random_nr) #sum of guesses    
#    if guessed_right > 0: total_right+=1
#prob = total_right/repeats
##comes out at 0.63, which is what we expected!

#birthday problem
#algebraic solution
k = 10
prob2 = 1 - (np.math.factorial(365)/np.math.factorial(365-k)/365**k)
#just over 50%, like we expected!

#simulation
repeats = 10**4 #how many times we want to repeat the experiment
total_right = 0
for i in range(repeats):
    random_bd = np.random.choice(365,k) #our sample, WITH REPLACEMENT!
    unique = np.unique(random_bd) #had to get creative here. we want to know if any 2 ppl share a bd, so here I'm checking if there are fewer unique values than just values
    if len(unique) < len(random_bd):
        total_right+=1
prob3 = total_right/repeats

