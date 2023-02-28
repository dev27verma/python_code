my_dict = {'name': 'dev', 'age': 27, 'address': 'Bengaluru', 'sex': 'male', 'mob': 8659, 'location': 'under'}

# pop
my_dict.pop('location')
print(my_dict)

# popitem() --> delete last item / 3.7 and before it used to delete any key-value randomly
my_dict.popitem()
print(my_dict)

# del --> delete specify key-value
del my_dict['age']
print(my_dict)

# clear --> delete all items --> return type is null
my_dict.clear()
print(my_dict)

# del --> delete the structure itself with all the items
del my_dict
# print(my_dict)  --> error - NameError: name 'my_dict' is not defined
