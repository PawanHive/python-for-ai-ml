'''
Take a decimal number as input (like 45.78) and output its :
- integer part - 45
- fractional part - .78
'''

n = float(input("enter a decimal number : "))

integer_part = int(n)
fractional_part = n - integer_part

print(f"integer part : {integer_part}")
print(f"fractional part : {round(fractional_part, 2)}")