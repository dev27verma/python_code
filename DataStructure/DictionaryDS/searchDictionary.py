# search

my_dict1 = {'name': 'dev', 'age': 27, 'address': 'Bengaluru'}
value = 27


def search_dict(my_dict, val):
    for key in my_dict:
        if my_dict[key] == val:
            return key, value
    return "Value not found"


print(search_dict(my_dict1, value))
