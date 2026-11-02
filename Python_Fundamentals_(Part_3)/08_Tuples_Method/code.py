# tuple methods

'''
.index(val)  ------ return 1st occurrence idx

.count(val) ------- counts total occurrences
'''

tup = (1, 2, 3, 10, 4)

for val in tup: 
  print(val)


# print sum of all tuple values

sum = 0
for val in tup:
  sum += val

print(f"sum of vals is {sum}")

'''
output: 
sum of vals is 20
'''

# find index and number of occurrence of val: 
tuple = (1, 2, 2, 3, 2, 4)

print(tuple.index(2)) # 1st occurrence of 2 will we shown as idx (at which index)
print(tuple.count(2))  # print number of occurrence of val 2

'''
output: 
1
3
'''