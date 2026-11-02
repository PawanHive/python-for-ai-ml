# Tuples: immutable sequence of values

tup = (1, 2, 3, 4, 5, "abc", 3.14)

print(tup)
print(type(tup))
print(tup[2])

'''
output: 
(1, 2, 3, 4, 5, 'abc', 3.14)
<class 'tuple'>
3
'''

# tup[2] = 10 # error: will not assign this value because tuple is immutable 

# how to create single value tuple
tup_single = (1,) # remember: comma behind single tuple is necessary and not required in multiple value tuples

print(tup_single)
print(type(tup_single))

'''
output: 
(1,)
<class 'tuple'>
'''

# tuple slicing

print(tup[0:3])
print(tup[:]) # print all tuple

'''
output:
(1, 2, 3)
(1, 2, 3, 4, 5, 'abc', 3.14)
'''