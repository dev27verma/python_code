my_list = [1, 'a', 2.4, 'text', ['a', 1], 'b']

# method 1
for i in my_list:
    print(i, end=' ')

print()

# method 2
for i in range(len(my_list)):
    print(my_list[i], end=' ')
