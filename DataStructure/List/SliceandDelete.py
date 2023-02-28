my_list = [1, 7, 4, 'f', 'a', 9, 'l', 2.4, 'text', ['a', 1], 'b']

# slice
print(my_list[0:2])

# update element using slicing
my_list[0:2] = ['x', 'y']
print(my_list)

'''-----------------------
Delete
------------------------'''
# delete if we know the value we use remove()
my_list.remove(9)
print(my_list)

# delete from last
my_list.pop()
print(my_list)

# delete from any index using pop
my_list.pop(2)
print(my_list)

# delete using delete()
del my_list[1]
print(my_list)

# delete using delete() slicing
del my_list[0:3]
print(my_list)
