## creating strings (can create using single, double and triple quotes)

name = "Pawan"
city = 'Varanasi'
message = """Hello! Welcome to python."""

print(name)
print(city)
print(message)

'''
output:
Pawan
Varanasi
Hello! Welcome to python.
'''

## find length of String

word = "Python"
print(len(word))

'''
output:
6
'''

## Concatenate String

word1 = "i love"
word2 = "javascript"
sentence = word1 + " " + word2
print(sentence)

'''
output:
i love javascript
'''

## Accessing characters using indexing

words = "python"
print(words[2])

'''
output: t
'''

## for loop on string

words = "Python"
for ch in words:
  print(ch)

'''
output:
p
y
t
h
o
n
'''

'''
Note:
string is immutable
'''