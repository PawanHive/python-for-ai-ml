# Dictionary Methods

'''
.keys() ------ returns all keys

.values()  ------- returns all values

.items()  ------ returns (key, val) pairs

.get(val) ----- returns val acc. to key

.update(new_item) ---- add new item to dictionary
'''

info = {
  "name": "shradha",
  "cgpa": 9.2,
  "subjects": ["math", "science"],
  3.14: "PI"
}

print(info.keys())
print(info.values())
print(info.items())

'''
output:
dict_keys(['name', 'cgpa', 'subjects', 3.14])
dict_values(['shradha', 9.2, ['math', 'science'], 'PI'])
dict_items([('name', 'shradha'), ('cgpa', 9.2), ('subjects', ['math', 'science']), (3.14, 'PI')])
'''

# know difference between using of [] method v/s .get() method ... while getting values of any keys 

# print(info["cgpa2"]) # #which not exit and will give ERROR and because of error stops next line execution 
print("end of code ")

'''
output:
KeyError: 'cgpa2'
'''

print(info.get("cgpa2")) # give 'None' and code and continue ahead
print("End OF CODE")

'''output: 
None
End OF CODE
'''

# add/insert key:value pair in dictionary
info.update({
  "city": "Delhi"
})

print(info)

'''
output: 
{'name': 'shradha', 'cgpa': 9.2, 'subjects': ['math', 'science'], 3.14: 'PI', 'city': 'Delhi'}
'''