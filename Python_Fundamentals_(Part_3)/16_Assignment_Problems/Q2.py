## Q2. Given a list of integers compute the average of all numbers in the list.

numbers = [10, 20, 30 , 40, 50]

total = 0 
count = 0

for num in numbers:
  total = total + num
  count = count + 1

average = total / count

print("Average: ", average)