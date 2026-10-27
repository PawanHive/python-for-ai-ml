'''
Write a function that takes two integers a and b and prints all even numbers between them (inclusive)
'''

def print_even(a, b):
  for i in range(a, b + 1):
    if i % 2 == 0:
      print(i)

print_even(3, 14)