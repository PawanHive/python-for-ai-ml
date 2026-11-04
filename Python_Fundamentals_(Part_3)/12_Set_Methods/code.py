# Set Methods

'''
.add(val) ---- adds a val

.remove(val) ---- removes a val

.clear() ---- empties the set

.pop() --- removes a random val

.union(set2) --- returns new union

.intersection(set2) ---- returns new intersection
'''

s = {1, 2, 2, 2, 3}

s.add(5)
s.remove(1)

print(s)
s.pop()
print(s)

s.clear()
print(s)

'''
output: 
{2, 3, 5}
{3, 5}
set()
'''

# lets look at union and intersection example 

s1 = { 1, 2, 3, 4, 5} 
s2 = {4, 5, 8, 9, 10}

print(s1.union(s2))  # all unique elements
print(s1.intersection(s2))

''''
output: 
{1, 2, 3, 4, 5, 8, 9, 10}
{4, 5}
'''