# functions in python

## Example

# this is function definition
def greet():
  print("Hello, Pawan!")

greet()   # this is function call

'''
output: Hello, Pawan!
'''


## Functions with Parameter and Argument

def greet1(name): # here 'name' is parameter
  print("Hello", name)

greet1("Suraj!") # here 'Suraj!' passes as argument

'''
output: Hello Suraj!
'''

## funcions with 'return' key

def add(a, b):
  return a + b

print(add(5, 6))

'''
output: 11
'''