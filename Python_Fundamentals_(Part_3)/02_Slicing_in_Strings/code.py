## Slicing 

'''
Syntax: 
string[start:stop:step]


start: index where extraction begins.
stop: index where extraction ends (excluded).
step: how many positions to move each time.
'''

word = "PYTHON"

print(word[0:3])
print(word[2:5])
print(word[:4])
print(word[2:])
print(word[::2])
print(word[::-1])

'''output: 
PYT
THO
PYTH
THON
PTO
NOHTYP
'''

## Negative indexing 
''' 
- Negative indexing starts from the end of the string. The last character has index -1.
'''

word = "python"

print(word[-1])
print(word[-2])
print(word[-6])
print(word[-6:-2])

'''
output:
n
o
p
pyth
'''