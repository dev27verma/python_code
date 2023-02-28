from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
print(arr1)

# insert at last

arr1.insert(6, 9)  # 5 is index 9 is value
print(arr1)

# insert at start

arr1.insert(0, 8)  # 0 is index 8 is value
print(arr1)

# insert at specific index

arr1.insert(4, 0)  # 4 is index 0 is value
print(arr1)
