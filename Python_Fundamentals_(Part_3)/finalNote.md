# 1. String in Python

## 1. Creating strings
- You can create a string using single quotes **(' ')**, double quotes **(" ")**, or triple quotes **(''' ''' or """ """)**.
```python
name = "Pawan"
city = 'Varanasi'
message = """Hello!Welcome to Python."""
print(name)
print(city)
print(message)
```
```
Output:
Pawan
Varanasi
Hello!
Welcome to Python.`
```

## 2. Find length of String
```python
word = "Python"
print(len(word))
```

```
output:
6
```

## 3. Accessing characters using indexing
- Each character in a string has an index (position). Python indexing starts at 0.

```python
words = "python"
print(words[2])
```

```
output: t
```

Note: string is immutable 

# 2. Slicing in Strings

- Slicing lets you extract a portion of a string.

Syntax: 
```syntax
string[start:stop:step]
```
- start: index where extraction begins.
- stop: index where extraction ends (excluded).
- step: how many positions to move each time.

```python
word = "PYTHON"

print(word[0:3])
print(word[2:5])
print(word[:4])
print(word[2:])
print(word[::2])
print(word[::-1])
```
```output: 
PYT
THO
PYTH
THON
PTO
NOHTYP
```

## Negative indexing 
- Negative indexing starts from the end of the string. The last character has index -1.

```python
word = "python"

print(word[-1])
print(word[-2])
print(word[-6])
print(word[-6:-2])
```
```
output:
n
o
p
pyth
```

# 3. String Formatting f-string and format()

## 1. String literals formatting (f-string)
- An f-string makes it easy to include variables inside a string. Put `f` before the opening quotation mark and place variables inside `{}`.
```python
name = "Pawan"
age = 23

print(f"My name is {name} and I am {age} years old.")
```
```
My name is Pawan and I am 23 years old.
```

# 4. Lists in Python

- a **list in python** is a built-in data structure used to store multiple items in a single variable.
- without a list, we might create five different variables
- but python allows us to store all these names in one variable using a list.

```python
students = ["Pawan", "Rahul", "Aman", "Priya", "Rohit"]

print(students)
```

```
['Pawan', 'Rahul', 'Aman', 'Priya', 'Rohit']
```

## 1. Creating a list

```python
# List of strings
names = ["Pawan", "Rahul", "Aman"]

# List of integers
numbers = [10, 20, 30, 40, 50]

# List of floats
prices = [10.5, 20.75, 30.99]

# Empty list
empty_list = []

print(names)
print(numbers)
print(prices)
print(empty_list)
```

**Important:** Python lists can contain different data types together.

```python
my_list = ["Pawan", 23, 85.5, True]

print(my_list)
```
```
['Pawan', 23, 85.5, True]
```

# 5. List Methods: 

## 1. adding elements to a list
### 1. `append()`

- the `append()` method adds one element at the end of the list.

```python 
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```
```
['Apple', 'Banana', 'Mango'
```

###  2. `insert()` 
- the `insert()` method adds an element at a specific position.

Syntax: 
```
list.insert(index, element)
```

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)
```

```
['Apple', 'Orange', 'Banana', 'Mango']
```

### 3. `sort()`
- `sort()` modifies the original list.

```py
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```
```
[10, 20, 30, 40]
```

### 4. `reverse()`

```py
nums = [1, 2, 3]

nums.reverse()
print(nums)
```

```
[3, 2, 1]
```

# 7. Tuples in Python: 

- a **tuple in python** is a build-in data structure used to store multiple items in a single variable.

Tuples are similar to lists, but there is one major difference:

Lists are mutable, whereas tuples are immutable.
- Mutable means you can modify the elements after creating the list.
- Immutable means you cannot modify the elements after creating the tuple.

```py
student = ("Pawan", 23, "India", 85.5)

print(student)
```

```
('Pawan', 23, 'India', 85.5)
```

## 1. Creating a tuple:
- You can create a tuple using parentheses `()` with elements separated by commas.

```py
# Tuple of strings
names = ("Pawan", "Rahul", "Aman")

# Tuple of integers
numbers = (10, 20, 30, 40, 50)

# Tuple of floats
prices = (10.5, 20.75, 30.99)

# Empty tuple
empty_tuple = ()

print(names)
print(numbers)
print(prices)
print(empty_tuple)
```

```
('Pawan', 'Rahul', 'Aman')
(10, 20, 30, 40, 50)
(10.5, 20.75, 30.99)
()
```

# 8. Tuples Method

### 1. `count()`
- The `count()` method returns how many times a particular element appears in a tuple.

```py
numbers = (10, 20, 30, 20, 40, 20)

print(numbers.count(20))
```

```
3
```

### 2. `index()`
- he `index()` method returns the index of the first occurrence of a specified element.
```py
fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits.index("Mango"))
```

```
2
```

# 9. Dictionary in Python
- A **dictionary** in Python is a built-in data type used to store data in **key-value pairs**.

Think of a real-world dictionary: you search for a word and get its meaning. Similarly, in a Python dictionary, you use a `key` to access its corresponding `value`.

## 1. Creating a dictionary:
- we use curly braces `{}` to create a dictionary.

```py
student = {
    "name": "Pawan",
    "age": 23,
    "course": "Python",
    "city": "Varanasi"
}

print(student)
```

```
{'name': 'Pawan', 'age': 23, 'course': 'Python', 'city': 'Varanasi'}
```

# 10. Dictionary Method

## 1. Accessing dictionary values: 
```py
student = {
    "name": "Pawan",
    "age": 23,
    "course": "Python"
}

print(student["name"])
print(student["age"])
```

```
Pawan
23
```

**Important:** If you try to access a key that doesn't exist, Python raises a KeyError.

```py
print(student["email"])
```

This produces a `KeyError` because `"email"` is not present.

### 1. Using `get()`

The`get()` method is a safer way to access values.
```py
print(student.get("name"))print(student.get("email"))
```
```
Pawan
None
```

### 2. Adding new key-value pairs

```py
student = {
    "name": "Pawan",
    "age": 23
}

student["city"] = "Varanasi"

print(student)
```

```
{'name': 'Pawan', 'age': 23, 'city': 'Varanasi'}
```

### 3. `update()`

- If a key already exists, assigning a new value updates its existing value.

```py
student = {
    "name": "Pawan",
    "age": 23
}

student["age"] = 24

print(student)

student.update({
    "age": 24,
    "city": "Varanasi"
})

print(student)
```
```
{'name': 'Pawan', 'age': 24, 'city': 'Varanasi'}
```

# 11. Set in Python
- A set in Python is a built-in data type used to store multiple unique values in a single variable.

- The most important feature of a set is that it does not allow duplicate elements.

- For example, if you have [10, 20, 20, 30, 30, 40], a set will automatically remove the duplicates.

## 1. Creating a set
- we are curly braces `{}` to create a set.

```py
numbers = {10, 20, 30, 40}

print(numbers)
```

```
{40, 10, 20, 30}
```

**Note:** The order of elements in a set is not guaranteed.

## 2. Creatign an empty set
**This is important**
```py
my_set = set()
print(my_set)
```
Output: 
```
set()
```
Why not use `{}`? Because `{}` creates an empty dictionary, not an empty set.

# 12. Set Method

## 1. Methods

```py
s = {1, 2, 2, 2, 3}

# add() - add one element
s.add(5)

# remove() - remove a specific element
s.remove(1)


print(s)

# pop() - removes and returns an arbitrary element.
s.pop()
print(s)

# clear() - removes all elements
s.clear()
print(s)
```

```
output: 
{2, 3, 5}
{3, 5}
set()
```

## 2. lets look at union and intersection example 
```py
s1 = { 1, 2, 3, 4, 5} 
s2 = {4, 5, 8, 9, 10}

print(s1.union(s2))  # all unique elements
print(s1.intersection(s2))
```
```
output: 
{1, 2, 3, 4, 5, 8, 9, 10}
{4, 5}
```
