# Lists: mutable sequence of values

marks1 = 99 
marks2 = 89
marks3 = 100
marks4 = 65
marks5 = 92

# OR 

marks = [99, 89, 100, 65, 92, "abc", 100.99]

print(marks)
print(marks[2])
print(len(marks))

marks[2] = 70 # re-assign the value change from 100 to 70 now 
print(marks)

print(type(marks)) # remember: we can store any type of data in list

'''
output: 
[99, 89, 100, 65, 92]
100
5
[99, 89, 70, 65, 92]
<class 'list'>
'''

# list Slicing: list[start:stop:step]

print(marks[0:6])
print(marks[5:len(marks)])
print(marks[-5:-2]) # this is negative index value

'''
output: 
v[99, 89, 70, 65, 92, 'abc']
['abc', 100.99]
[70, 65, 92]
'''

# How to create single value list
list_single = [1]

print(list_single)
print(type(list_single))

'''
output:
[1]
<class 'list'> 
'''