my_list = [1, 'a', 2.4, 'text', ['a', 1], 'b']

# update an element

my_list[0] = 55
print(my_list)

# -------------------------------------------------
# Insert an element at any index

my_list.insert(0, 22)
print(my_list)

# insert at last

my_list.append(65)
print(my_list)

# insert another list

new_list = [1, 4, 6, [22, 5]]
my_list.extend(new_list)
print(my_list)
