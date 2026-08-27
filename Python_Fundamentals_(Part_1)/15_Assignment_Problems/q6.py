'''
Q6. Write a program to swap values of two numbers entered by the user.
'''
# solved using 'temp' variable

'''
a = input("enter value of a : ")
b = input("enter value of b : ")

temp = a
a = b
b = temp

print(f"value of a : {a}")
print(f"value of b : {b}")
'''

# without using 'temp' variable 

a = input("enter value of a : ")
b = input("enter value of b : ")

a, b = b, a   # python do this automatically using python tuple unpacking

print(f"value of a : {a}")
print(f"value of b : {b}")