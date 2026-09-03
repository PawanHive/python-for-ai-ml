# break keyword :

i = 1
while (i <= 10):
  if (i % 6 ==0): # break loop execution at 6 multiple
    break
  print(i)
  i += 1

print("outside loop now...")

# conditinue keyword:
# print 1 to 10 number but skip multiple of 3 
i = 1
while (i <= 10):
  if (i % 3 == 0): # skip all num which is multiple of 3
    i += 1
    continue
  print(i)
  i += 1
  print("outside loop now...")

# print odd number between 1 - 10
i = 0
while (i < 10):
  i += 1
  if (i % 2 == 0):
    continue
  print(i)