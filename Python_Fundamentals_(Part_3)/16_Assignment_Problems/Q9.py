'''Q9. Given a list, print all elements that appear more than once in the list.

[Hint - use sets]'''

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

seen = set()
duplicates = set()

for num in numbers:
  if num in seen:
    duplicates.add(num)
  else:
    seen.add(num)

print("Duplicate elements:", duplicates)

