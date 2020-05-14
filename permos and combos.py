from itertools import permutations as P, combinations as C, combinations_with_replacement as CR

substrate = [2,3,4,5,6,7,8,9,10]
choose = 3
##permutations (order matters) w/ replacement
#perm_rep = choose**len(substrate)
#print('permutations w/ replacement')
#print(perm_rep)
#print(' ')
#
##permutations (order matters) NO replacement
#print('permutations NO replacement')
#perm = P(substrate,choose)
#count = 0
#for i in list(perm):
#    count+=1
##    print(i)
#print(count)
#print(' ')
    
#combinations (order does NOT matter) w/ replacement
print('combinations w/ replacement')
comb = CR(substrate,choose)
count = 0
for i in list(comb):
    count+=1
    print(i)
print(count)
print(' ')

#combinations (order does NOT matter) NO replacement
#print('combinations NO replacement')
#comb = C(substrate,choose)
#count = 0
#for i in list(comb):
#    count+=1
##    print(i)
#print(count)
#print(' ')

#when probability is different
#use np.random.choice