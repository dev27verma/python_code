my_dict1 = {'name': 'dev', 'age': 27, 'address': 'Bengaluru', 'sex': 'male', 'mob': 8659, 'location': 'under'}

# copy - it copies the dictionary
my_dict2 = my_dict1.copy()
print(my_dict1)
print(my_dict2)

# fromkeys() it create a new dict from given sequence
my_dict3 = {}.fromkeys([1, 2, 3], [0, 2, 3])
print(my_dict3)
my_dict4 = {}.fromkeys([1, 2, 3], 0)
print(my_dict4)
my_dict5 = {}.fromkeys([1, 2, 3])
print(my_dict5)

# get()
print(my_dict1.get('age'))
print(my_dict1.get('city'))  # city is not present in dict
print(my_dict1.get('city', 24))  # city is not present in dict, it just print the value

# items - return key-value pair in the form of tuple
print(my_dict1.items())

# keys - return all keys
print(my_dict1.keys())

# values()
print(my_dict1.values())

# update
my_dict1.update(my_dict3)
print(my_dict1)

# setdefault() --> return value if key is present else add key
my_dict1.setdefault('age', 86)
print(my_dict1)
my_dict1.setdefault('city', 'golem')
print(my_dict1)
