from itertools import permutations as P, combinations as C, combinations_with_replacement as CR
import numpy as np

won = 0
#for i in range(10**4):
#    choices = [1,2,3,4,5]
#
#    last = np.random.choice(choices,1)
#
#    first = np.random.choice(choices,1)
#    choices.remove(first)
#
#    second = np.random.choice(choices,1)
#    choices.remove(second)
#
#    third = np.random.choice(choices,1)
#    choices.remove(third)
#
#    forth = np.random.choice(choices,1)
#    choices.remove(forth)
#
#    if choices[0] == last:
#        won+=1
#prob=won/10**4
#so he gets his seat in about 1/3 of cases

for i in range(10**4):
    choices = [1,2,3,4,5]
    allocated = [5,4,3,2,1]

    first = allocated[0]
    second = allocated[1]
    third = allocated[2]
    forth = allocated[3]
    last = allocated[4]

    first = np.random.choice(choices,1)
    choices.remove(first)

    if second in choices:
        choices.remove(second)
    else:
        second = np.random.choice(choices,1)
        choices.remove(second)

    if third in choices:
        choices.remove(third)
    else:
        third = np.random.choice(choices,1)
        choices.remove(third)

    if forth in choices:
        choices.remove(forth)
    else:
        forth = np.random.choice(choices,1)
        choices.remove(forth)

    if choices[0] == last:
        won+=1
prob=won/10**4