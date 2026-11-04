# Q1: Ask the user for a string and check whether it is a palindrome or not.
'''
Definition: A palindrome is a string which is the same when we read it forward & backward (e.g., "madam", "racecar", etc.).

Hint: A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually.
'''

user_input = input("Enter a string: ")

reversed_string = ""

for char in user_input:
  reversed_string = char + reversed_string

if user_input == reversed_string:
  print("It is a palindrome.")
else: 
  print("It is not a palindrome.")