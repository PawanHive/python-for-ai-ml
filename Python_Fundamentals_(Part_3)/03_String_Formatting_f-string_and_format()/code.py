# String formatting

a = 5 
b = 10
sum = a + b 

# normal formatting 
print("sum is {}".format(sum))
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))

'''
output: 
sum is 15
language is python
sum of 5 & 10 is 15
'''

# index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))

'''
output: 
sum of 10 & 5 is 15
'''

# value based formatting: (we can reuse value at any place)
print("values of vars {a} & {b}".format(a=5, b=10))
print("{b}values of vars {a} & {b}".format(a=5, b=10))

'''output:
values of vars 5 & 10
10values of vars 5 & 10
'''

# string literals formatting ( f-string )
print(f"sum is {sum}")

'''
output: 
sum is 15
'''