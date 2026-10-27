'''
Q4. Write a function to return the count of the number of digits in a number, n.
'''

def count_digits(n):
  n = abs(n)
  count = 0

## base case
  if n == 0:
    return 1
  
  while (n > 0):
    count = count + 1
    n = n // 10
  return count

print(count_digits(0))
