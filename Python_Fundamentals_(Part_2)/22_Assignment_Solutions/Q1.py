'''
Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules: 
- if salary < 30,000 -> 5%
- if salary is 30,000 -70,000 -> 15%
- if salary > 70,000 -> 25%
'''

salary = float(input("enter salary: "))

if salary < 30000:
  tax_rate = 5
elif salary <= 70000:
  tax_rate = 15
else:
  tax_rate = 25

print (f"Tax rate = {tax_rate}%")


