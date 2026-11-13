'''
Q4. Given a tuple of integers, create:

A tuple of all even numbers
A tuple of all odd numbers
'''

numbers = (10, 15, 20, 25, 30, 35, 40, 45)

even_numbers = ()
odd_numbers = ()

for num in numbers: 
  if num % 2 == 0:
    even_numbers = even_numbers + (num,)
  else:
    odd_numbers = odd_numbers + (num,)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)