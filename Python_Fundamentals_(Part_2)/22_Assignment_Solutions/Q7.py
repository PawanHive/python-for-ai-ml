'''
Q7. Design a program to continuously input a number n from user & print if it is positive or negative until the user enters "Quit".
'''

while True:
  n = input("Enter a number (or Quit to exit): ")

  if n == "Quit":
    break 

  n  = int(n)

  if n > 0: 
    print("Positive")
  elif n < 0:
    print("Negative")
  else:
    print("Zero")