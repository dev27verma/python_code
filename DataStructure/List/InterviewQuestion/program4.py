# What will be the output of the following code block?

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = 10, 20, 30, 40, 50, 60
print(a)

'''
Option:
a. [10, 2, 20, 4, 30, 6, 40, 8, 50, 60]
b. [1, 10, 3, 20, 5, 30, 7, 40, 9, 50, 60]
c. ValueError: attempt to assign sequence of size 6 to extended slice of size 5
d. [1, 2, 10, 20, 30, 40, 50, 60]

'''