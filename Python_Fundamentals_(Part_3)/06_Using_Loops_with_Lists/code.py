# lists loops 
## we can use a loop to access every element in a list

nums = [1, 2, 3, 10, 4]

for val in nums: 
  print(val)

'''
output: 
1
2
3
10
4
'''

# find index of x nubmer
x = 10
idx = 0
for val in nums: 
  if (val == x):
    print(f"x found at idx = {idx}")
    break
  idx = idx +1

'''
output: 
3
'''