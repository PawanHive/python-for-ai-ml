'''
Q3. Input two lists of integers from the user. Merge them into one list and sort the result.

Eg - list1 = [1, 2, 7], list2 = [2, 4, 5] -> result = [1, 2, 3, 54, 5, 7]
'''

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list1 + list2

result.sort()

print("Merged and sorted list: ", result)