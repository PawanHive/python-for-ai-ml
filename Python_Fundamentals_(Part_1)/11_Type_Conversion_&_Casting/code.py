# Type conversion
## 1. implicit conversion (python do automatically) eg. float val + int val = float ans

a = 10
b = 5
print (a / b) # output: 2.0 ( this is floating value)
print (type (a / b)) # output: float

## 2. explicit conversion (type casting) -- developer do forcefully 

ans1 = int(5 + 10.0) # casting
ans2 = 5 + 10.0 # conversion by python automatically

print(ans1, type(ans1)) # 15 int
print(ans2, type(ans2)) # 15.0 float

## `False` = 0  and `True` = any non-zero value
val = bool(0)
val1 = bool(10)
print (val, type(val)) # False bool
print (val1, type(val1)) #True bool
