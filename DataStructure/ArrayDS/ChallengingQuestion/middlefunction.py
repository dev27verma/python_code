# Write a function called middle that takes a list and returns a new list that contain all except first and last element

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def middle(lst):
    result = []
    for i in range(lst[1], len(lst)):
        result.append(i)
    return result


print(middle(my_list))


# using slicing
'''
def middle(lst):
    return lst[1:-1]


print(middle(my_list))
'''