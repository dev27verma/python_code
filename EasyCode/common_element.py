'''write python code to find comon element between two list
list1 = [1,2,3,4]
list2 = [3,4,5,6]

output : [3,4]
'''

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = list(set(list1) & set(list2))

print(result)