# Find the value in the array?

import numpy as np

element = int(input("Enter the length of array: "))
my_list = []
for i in range(element):
    my_list.append(int(input("Enter Value: ")))
array1 = np.array(my_list)

print(array1)

search_element = int(input("Enter the value to search: "))


def search(arr, s):
    for i in range(len(arr)):
        if arr[i] == s:
            return "Value found at index: " + str(i)
    return "Value not present in array"


print(search(array1, search_element))
