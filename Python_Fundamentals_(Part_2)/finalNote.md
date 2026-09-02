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

# 6.1: Remember Indentation effect in python
- indentation defines a block of code.
- same indentation - same block
- more indentation - inside the previous block
- less indentation - outside the block
- python uses indentation instead of `{}`