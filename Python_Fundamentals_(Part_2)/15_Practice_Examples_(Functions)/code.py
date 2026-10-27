# calculate average of 3 numbers

def calc_avg(a, b, c):
  sum = a + b + c
  return sum/3

print(calc_avg(3, 4, 5))
'''
output: 4.0
'''

## default parameter in python

def sum(a, b=1):     # remember: non-default parameter first -> then default parameter later
  return a + b

print(sum(5))  # output: 6
print(sum(5, 6)) # output: 11
''