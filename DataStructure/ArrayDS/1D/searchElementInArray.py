from array import *

element = int(input("Enter the number of element to enter: "))
array1 = array('i', [])
for i in range(element):
    array1.append(int(input("Enter the element: ")))

val = int(input("Enter the value to find: "))


def search_element_in_array(arr, value):
    for i in arr:
        if i == value:
            return arr.index(val) + 1
    return "Value not available"


print(f"Value is found at index: {search_element_in_array(array1, val)}")
