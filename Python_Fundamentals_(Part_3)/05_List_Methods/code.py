# Lists Method 

'''
.append(val) --------- add one element at the end
.insert(idx, val) ------- insert element at idx
.sort() ---------- arranges in increasing order
.reverse() ---------- reverses order

'''

nums = [1, 2, 3]

nums.append(4)
print(nums)

nums.insert(2, 10)
print(nums)

nums.reverse()
print(nums)

nums.sort() # sort in increasing order
print(nums)

nums.sort(reverse=True) # sort in decreasing order (reverse)
print(nums)

'''
output: 
[1, 2, 3, 4]
[1, 2, 10, 3, 4]
[4, 3, 10, 2, 1]
[1, 2, 3, 4, 10]
[10, 4, 3, 2, 1]
'''