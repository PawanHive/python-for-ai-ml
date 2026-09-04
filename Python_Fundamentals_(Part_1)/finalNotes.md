![Python_fundamental_(part_1)-1](../images/Python_fundamental_(part_1)-1.png)
![Python_fundamental_(part_1)-2](../images/Python_fundamental_(part_1)-2.png)


# 1. Python Indentifer rules

- Can contains letters (A-Z, a-z)
- Can contain digits (0-9)
- Can contain underscore (\_)
- Cannot start with a digit
- Cannot contain spaces
- Cannot use special characters like @, #, $, %, -
- Cannot be a Python keyword such a `if`, `for`, `class`, `while`, `true`, etc.
- Python Identifers are case-sensitive.

# 2. Data Types in Python

- Integer -> Represents whole number such a +ve, -ve, or zero
- Float -> Represents numbers with decimal values
- String -> Represents text or a sequence of characters.
- Boolean -> Represents logical values: `True` or `False`
- None -> Represents the absence of values.

# 3. Keywords in Python

| keyword  | keyword  | keyword |
| -------- | -------- | ------- |
| False    | finally  | try     |
| None     | for      | while   |
| True     | from     | with    |
| and      | global   | yield   |
| as       | if       | case    |
| assert   | import   |         |
| async    | in       |         |
| await    | is       |         |
| break    | lambda   |         |
| class    | match    |         |
| continue | nonlocal |         |
| def      | not      |         |
| del      | or       |         |
| elif     | pass     |         |
| else     | raise    |         |
| except   | return   |         |

# 4. Comments in Python
```py
# this is single line comment
```

```py
'''this is a multi-line comment
'''
```

# 5. Style Guide
- use `4 spaces` for indentation
- Use `snake_case` for variables and functions
- Use `PascalCase` for class names.
- Keep lines reasonably short. (80 character)
- Use meaningful and descriptive names.
- Put spaces around operators.
- Use blank lines to separate different sections of code.
- Write comments when the help explain why something is being done.

Note: Google recommends running `pylint` to find bugs and style problems.


# 6. Arithmeti Operator: 
`-` - Subtraction
`+` - Addition
`*` - Multiplication
`/` - Division
`%` - Modulo (give us remainder value)
`**` - this is basically (a ** b) means 'a' to the power 'b' ..... mean 'a' will multiply 'b' times

# 7. Relational Operator: 
`<` - less than 
`>` - greater than
`<=` - less than equal to
`>=` - greater than equal to
`==` - equal to 
`!=` - not equal to

# 8. Assignment Operator: 
 `=` -   Assign                  
 `+=` -   Add and assign          
 `-=`  -  Subtract and assign     
 `*=`  -  Multiply and assign     
 `/=`   - Divide and assign       
 `//=` -   Floor divide and assign 
 `%=` -   Modulo and assign       
 `**=` -  Power and assign        

# 9. Logical Operator: 
`and` - True if both conditions are True
`or` - True if at least one condition is True
`not` - Reverses the result 

# 10. Operator Precedence: 

| Priority | Operator                         | Meaning                 |
| -------: | -------------------------------- | ----------------------- |
|        1 | `()`                             | Parentheses             |
|        2 | `**`                             | Exponent                |
|        3 | `+x`, `-x`                       | Unary plus/minus        |
|        4 | `*`, `/`, `//`, `%`              | Multiplication/division |
|        5 | `+`, `-`                         | Addition/subtraction    |
|        6 | `<`, `>`, `<=`, `>=`, `==`, `!=` | Comparisons             |
|        7 | `not`                            | Logical NOT             |
|        8 | `and`                            | Logical AND             |
|        9 | `or`                             | Logical OR              |

# 11. Common Type Conversion

| Function  | Converts to | Example                           |
| --------- | ----------- | --------------------------------- |
| `int()`   | Integer     | `int("10")` → `10`                |
| `float()` | Float       | `float("10")` → `10.0`            |
| `str()`   | String      | `str(10)` → `"10"`                |
| `bool()`  | Boolean     | `bool(1)` → `True`                |

# Taking User Input: 
| Code                        | Purpose                      |
| --------------------------- | ---------------------------- |
| `input()`                   | Take user input as a string  |
| `int(input())`              | Take integer input           |
| `float(input())`            | Take decimal/float input     |

# 12. f-string : (formatted String Literal)

-   **F-string** = Formatted String Literal.
-   Used to **insert variables/expressions directly into a string**.
-   Add `f` before the string and put variables inside `{}`.

``` python
name = "Pawan"
age = 24

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

``` text
My name is Pawan and I am 24 years old.
```

**Syntax:**

``` python
f"Text {variable}"
```

# 13. SWAP two numbers

a = input("enter value of a : ")
b = input("enter value of b : ")

a, b = b, a   # python do this automatically using python tuple unpacking (without 'temp' variable)

print(f"value of a : {a}")
print(f"value of b : {b}")