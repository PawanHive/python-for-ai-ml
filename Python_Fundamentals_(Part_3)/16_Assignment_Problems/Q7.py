## Q7. Write a program that takes a string from the user and prints the number of spaces in the string.

user_input = input("Enter a strings: ")

count = 0

for char in user_input:
  if char == " ":
    count = count + 1

print("Number of spaces: ", count)

