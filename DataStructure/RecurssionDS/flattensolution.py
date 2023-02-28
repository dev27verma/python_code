my_list1 = [1, 2, 3, [4, 5]]
my_list2 = [1, 2, [3, 4], [[5]], [[[[[[6]]]]]]]
my_list3 = [[1], [2], [3], [4,5,[[6],7]]]
my_list4 = [[[1], [[[2]]], [[[[[[3]]]]]]]]


def flatten(arr):
    result_arr = []
    for custom_item in arr:
        if type(custom_item) is list:
            result_arr.extend(flatten(custom_item))
        else:
            result_arr.append(custom_item)
    return result_arr


print(flatten(my_list1))
print(flatten(my_list2))
print(flatten(my_list3))
print(flatten(my_list4))

'''
I/P

[1,2,3,[4,5]]                       0/p [1,2,3,4,5]
[1,2,[3,4],[[5]]]                   O/P [1,2,3,4,5]
[[1],[2],[3]]                       O/P [1,2,3]
[[[1],[[[2]]],[[[[[[3]]]]]]]        O/P [1,2,3]
'''
