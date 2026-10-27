# write a function to print the factorial of any number 'n'.

def calc_factorial(n):
  fact = 1
  for i in range (1, n + 1):
    fact = fact * i

  return fact

n = int(input("enter n: "))
print(calc_factorial(n))