# first example: 
'''
age = int(input("enter your age : "))

if (age < 13):
  print("child")
elif (age >= 13) and (age < 18):
  print("teenager")
else: 
  print("adult")
'''

# Second Example: 
'''
username = input("enter username : ")
password = input("enter password : ")

if (username == "pawan" and password == "Pawan@123"): 
  print("You logged in, Successfully.")
elif (username != "pawan"):
  print("wrong Username")
else: 
  print("wrong password")
'''

# Third Example: n is multiple of 5 or not?

n = int(input("enter num : "))

if (n % 5 == 0):
  print(f"{n} is multiple of 5")
else:
  print(f"this number {n}, is not multiple of 5")
