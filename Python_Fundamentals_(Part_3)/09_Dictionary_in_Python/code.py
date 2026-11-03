# Dictionary in Python: dictionary is a mutable

info = {
  "name": "shradha",
  "cgpa": 9.2,
  "subjects": ["math", "science"],
  3.14: "PI"
}
info["cgpa"] = 9.6

print(type(info))
print(info["cgpa"])
print(info["name"])
print(info[3.14])

'''output:
<class 'dict'>
9.6
shradha
PI
'''