# Q1. Write a program that asks the user for their name and age, then prints a sentence like:
# Output we want : Hello Shradha, you are 21 years old!

name = input("enter your name : ")
age = input("enter your age : ")

print("Hello", name,", you are", age,"years old!") # output: Hello Shradha , you are 21 years old!
# print in this way gives extra space between 'Shradha' and ',' comma so we will use f-String to solve this problem

print(f"Hello {name}, you are {age} years old!") # output: Hello Shradha, you are 21 years old!
# output: using f-string is perfect now 

# f-string a (formatted string literal)