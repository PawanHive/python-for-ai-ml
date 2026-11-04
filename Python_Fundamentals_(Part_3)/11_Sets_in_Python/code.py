# Set: collection of unique elements and can be unordered

s = {1, 2, 2, 2, 3} # as set store only unique element, thats why duplicate 2 will not count

print(len(s))

'''output:
3
'''

# how to add element in set
s.add(5)
print(s)

'''
output: 
{1, 2, 3, 5}
'''

# How to create empty set

empty_set = {} # we thought it is set but it is actually a <dictionary>
print(type(empty_set))

'''output:
<class 'dict'>
'''

empty_set1 = set() # this is how actually a empty set creates (using constructor function)
print(type(empty_set1))

'''
output:
<class 'set'>
'''