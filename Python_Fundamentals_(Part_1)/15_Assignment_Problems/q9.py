'''
Ask the user for : Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest: 

formula is : SI = (P * R * T) / 100
'''

P = float(input("enter Principal : "))
R = float(input("enter Rate : "))
T = float(input("enter Time : "))

SI = (P * R * T) / 100

print(f"simple interest is : {SI}")