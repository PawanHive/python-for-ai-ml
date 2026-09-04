# for loop

# for loop with strings

## here 'in' => membership operator (for each item 'in' collection/something)
string = "Hello"
for var in string:
  print(var)
'''
output: 
H
e
l
l
o
'''

# check 'o' exist in 'string' variable

if ('o' in string):
  print("o exists in string")

    ## - so it means we can also use 'in' keyword in our conditional statement
'''
output:
o eixts in string
'''

# for loop with sequence (print 0 to 5 number in a sequence)

for i in range(5):
  print(i)
'''
output:
0
1
2
3
4
'''

# print 'pawan' 5 times using for loop

for i in range(5):
  print("pawan")

'''
output:
pawan
pawan
pawan
pawan
pawan
'''

# How many times 'i' letter occur in these phrase = "artificial intelligence"

phrase = "artificial intelligence"

ans = 0

for letter in phrase:
  if (letter == "i"):
    ans = ans + 1

print(f"count of letter i = {ans}") 

'''
output: 
count of letter i = 5
'''