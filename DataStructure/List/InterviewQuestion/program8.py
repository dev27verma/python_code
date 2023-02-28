# What will be the output of the following code block?

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v


print(fun(data[0]))

'''
Options:
a. 5
b. 3
c. 4
d. 1
e. 6
f. 2
'''
