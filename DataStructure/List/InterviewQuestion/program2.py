# What will be the output of the following code block?

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end=" ")

'''
Options:
a. 2 3 4 5 6 1
b. 1 1 2 3 4 5
c. 2 3 4 5 6 6
d. 1 2 3 4 5 6
'''