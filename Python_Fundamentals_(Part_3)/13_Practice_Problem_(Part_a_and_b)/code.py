# Questions is : 
'''
Student Enrolments

Given a list of tuples with info (name, subject):

List all unique courses
List students enrolled in English
Create dictionary (student, set of courses)
'''

info = [
  ("Alice", "Math"),
  ("Bob", "Science"),
  ("Alice", "Science"),
  ("Charlie", "Math"),
  ("Bob", "Math"),
  ("Alice", "English"),
  ("Charlie", "English"),
]

##  List all unique courses

courses_set = set() # empty set defined

for tup in info:
  courses_set.add(tup[1]) # course

print(courses_set)

'''
output: 
{'Science', 'English', 'Math'}
'''

## List students enrolled in English

for name, course in info:
  if(course == "English"):
    print(name)

'''
output: 
Alice
Charlie
'''

## Create dictionary (student, set of courses)

dict = {}

for name,course in info:
  if(dict.get(name) == None):
    dict.update({name: set()})
    dict[name].add(course)
  else:
    dict[name].add(course)

print(dict)

'''
output: 
{'Alice': {'Science', 'English', 'Math'}, 'Bob': {'Science', 'Math'}, 'Charlie': {'English', 'Math'}}
'''