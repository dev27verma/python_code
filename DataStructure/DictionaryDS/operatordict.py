my_dict1 = {'name': 'dev', 'age': 27, 'address': 'Bengaluru', 'sex': 'male', 'mob': 8659, 'location': 'under',
            1: [0, 2, 3], 2: [0, 2, 3], 3: [0, 2, 3], 'city': 'gleam'}

# IN Operator
print('name' in my_dict1)
print('dev' in my_dict1.values())

# for operator
for keys in my_dict1:
    print(keys, my_dict1[keys], end=' ')
print()
# all()
my_dict2 = {1: True, 2: True, 3: True, 4: True}
print(all(my_dict2))
my_dict3 = {1: True, 2: False, 3: False, 4: False}
print(all(my_dict3))
my_dict4 = {1: False, 2: True, 3: True, 4: True}
print(all(my_dict4))
my_dict5 = {1: False, 2: False, 3: False, 4: False}
print(all(my_dict5))
my_dict6 = {}
print(all(my_dict6))

# sorted
my_dict7 = {'d': 1, 'b': 7, 'a' : 6, 'e': 2, 'c': 3}
print(sorted(my_dict7))
print(sorted(my_dict7,reverse=True))