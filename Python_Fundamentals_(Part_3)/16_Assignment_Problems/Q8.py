'''
Q8. Write a program to check whether two lists share no common elements.

Python
# share no common elements
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# share common elements
list1 = [1, 2, 3]
list2 = [3, 4]
[Hint - use sets]
'''

# input lists 
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# convert lists into sets
set1 = set(list1)
set2 = set(list2)

# check for common elements
if set1.isdisjoint(set2):
  print("Lists share no common elements.")
else:
  print("Lists have common elements.")