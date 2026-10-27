'''
Write a function to return the sum of digits of a number, n.
'''

def sum_digits(n):

  total = 0

  while (n > 0):
    digit = n % 10
    total = total + digit 
    n = n // 10

  return total

print(sum_digits(312))