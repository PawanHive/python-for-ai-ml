![Python_Fundamentals_(Part_2)-1](../images/Python_Fundamentals_(Part_2)-1.png)
![Python_Fundamentals_(Part_2)-1](../images/Python_Fundamentals_(Part_2)-2.png)

# 1: Conditional Statement in Python
- Used to make decisions based on a condition.
`if` - Execute when condition is **True**. (`if` or `if-else` or **nested** `if`)
`elif` - Checks another condition.(`if-elif-else`)
`else` - Executes when all conditions are **False**.

Syntax: 

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

# 2: n is multiple of 5 or not?
**Formula:** `n % 5 == 0`

# 3: n is EVEN or ODD
Every EVEN number is completely divisible by 2.

```python
if (n % 2 == 0):
  print("EVEN")
else:
  print("ODD")
```

# 4: Nesting
```python
username = input("enter username : ")
password = input("enter password :")

if (username == "pawan" and password == "Pawan@123"):
  print("Loggin Successfully")
else: 
  if (username != "pawan"):
    print("wrong username")
  else: 
    print("wrong password")
```

# 5: `match-case` in python
- it is similar to `switch-case` in languages like JavaScript/Java

**Syntax:**
```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

**Example:**
```python
color = input("enter color : ")

match color : 
  case "green":
    print("Go")
  case "yellow":
    print("Slow")
  case "red":
    print("Stop")
  case _:
    print("Wrong color!")
```

# 6: Loops using while:
- `while` loop - repeats a block of code as long as the condition is `True`
- The condition is checked **before every iteration**.

**Syntax:**
```python
while condition: 
  # code
```

**Example:** print "hello world" 5 times
```python
count = 1

while (count <= 5):
  print("hello world", count)
  count = count + 1 

print("after loop, count = ", count) 
```

**More Examples:**
```python
# print 1 to 5 number using while loop
i = 1 
while (i <= 5):
  print(i)
  i += 1
print("printed")

# print reverse 5 to 1 
i = 5
while (i >= 1):
  print(i)
  i -= 1
print("printed reverse")
```

# 7: Remember Indentation effect in python
- indentation defines a block of code.
- same indentation - same block
- more indentation - inside the previous block
- less indentation - outside the block
- python uses indentation instead of `{}`

# 8: Multiplication Table of any number `n`
```python
n = int(input("enter number : "))

i = 1; 
while ( i <= 10): 
  print(f"{n} * {i} = {n*i}")
  i += 1
```

# 9: Break and Continue
## `Break`
- Stops the loop completely.
- Execution continues after the loop.
**Examples:**
```python
i = 1
while (i <= 10):
  if (i % 6 ==0):
    break
  print(i)
  i += 1
```

## `continue`
- Skips the current iteration and moves to the next iteration.
**Examples:**
```python
# print odd number between 1 - 10
i = 0
while (i < 10):
  i += 1
  if (i % 2 == 0):
    continue
  print(i)
```

# 10: loops using `for`

- **for loop** - repeats code for each item in a sequence.
- `in` - takes each item **one by one** from the sequence and also use in conditional statement to check item exits or not.

**Syntax**
```python
for variable in sequence:
  # code
```

**Example:**
```python
for i in range(5):
  print(i)
```
output: 
```terminal
0
1
2
3
4
```

**Remember:** `for x in collection` = "for each x/item in the collection/sequence/something"

## 10.1: `in` keyword used in both `for` loops and conditional statements.

### 1. in `for` loop
- `in` means **"take each item from"**
```python
for letter in "apple":
  print(letter)
```
output:
```terminal
a
p
p
l
e
```

### 2. in conditional statement
- `in` means **"is this item exits/present inside?"**
```python
if "a" in "apple":
  print("found")
```
output:
```terminal
found
```

## 10.2: How many times 'i' letter occur in these phrase = "artificial intelligence"
```python
phrase = "artificial intelligence"

ans = 0

for letter in phrase:
  if (letter == "i"):
    ans = ans + 1

print(f"count of letter i = {ans}") 
```
output: 
```terminal 
count of letter i = 5
```

# 11: count number of vowel present in word="artificial" 

```python
word = "artificial"

count = 0

for ch in word:
  if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    count = count + 1

print("ans : ", count)
```

output: 
```terminal
ans : 5
```

# 12: range() function

## 1. range(stop)
- Starts from `0` and goes up to `stop - 1`.

```python
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```

## 2. range(start, stop)
- Starts from `start` and goes up to `stop - 1`.

```python
for i in range(2, 6):
    print(i)
```
Output:
```
2
3
4
5
```

## 3. range(start, stop, step)
- `step` tells Python how much to **increase/decrease** each time.

```python
for i in range(0, 10, 2):
    print(i)
```
Output:
```
0
2
4
6
8
```

**Remember**
`range(start, stop, step)`

`start` → where to start
`stop` → where to stop (not included)
`step` → how much to jump

👉 The `stop` value is always excluded.

# 13. Sum of N numbers

```python
n = int(input("enter number : "))

sum = 0

for i in range(1, n+1):
  sum += i
print ("sum =", sum)
```

the function of formula for sum of the first N natural numbers is : `f(n) = n(n + 1) / 2`

# 14. Functions in Python
- A **function** is a reusable block of code that performs a specific task.
- instead of writing the same code again and again, we **define it once** and **call it whenever needed**.

**Syntax:**
```python
def function_name():
  # code
```

## 1. Example
```python
def greet():  # this is function definition
  print("Hello, Pawan!")

greet()   # this is function call
```
```
output: Hello, Pawan!
```


## 2. Functions with `Parameter` and `Argument`

```python
def greet1(name): # here 'name' is parameter
  print("Hello", name)

greet1("Suraj!") # here 'Suraj!' passes as argument
```
```python
output: Hello Suraj!
```

## funcions with `return`
```python
def add(a, b):
  return a + b  # 'return' will send result back

print(add(5, 6))  # 5, 6 = argument
```
```python
output: 11
```

### Remember
`Parameter` = receive input to a function **(placeholder)**
`Argument` = actual values we pass **(actual value)**
`Return` = sends the result back from a function **(output)**

# 15. Default Parameter in Python
- a **default parameter** is a parameter that already has a **default value**. if the caller doesn't provide a value, Python uses that **default**.

```python
def sum(a, b=1):  
  return a + b

print(sum(5, 6)) # output: 11
print(sum(5))  # output: 6
```

### Remember 
**Required parameter first → Default parameter later**

```
def function(required, default):
              ↑          ↑
           non-default   has default
```

# 16. Types of Functions
`Built-in` = **Python gives it**
`User-defined` = **You create it**

# 17. `lambda` functions
- a `lambda function` is a **small anonymous function** (a function without a name) used for simple operations

**Syntax:**
```python
lambda parameters: expression
```

**Normal functions:**
```python
def sum(a, b):
  return a + b

print(sum(1, 2))
```

**`lambda` functions:**
```python
sum = lambda a, b: a + b
print(sum(3, 4))
```

# 18. Factorial of N

```python
def calc_factorial(n):
  fact = 1
  for i in range (1, n + 1):
    fact = fact * i

  return fact

n = int(input("enter n: "))
print(calc_factorial(n))
```
```terminal
output:
enter n: 5
120
```