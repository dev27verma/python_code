# What will be the output of the following code block?

def f(i, values=[]):
    values.append(i)
    print(values)
    return values


f(1)
f(2)
f(3)

'''
Options:
a. [1] [1, 2] [1, 2, 3]
b. [1] [2] [3]
c. 1 2 3
d. [1, 2, 3]
'''
