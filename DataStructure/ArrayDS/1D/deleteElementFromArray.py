from array import *

element = int(input("Enter the number of element to enter: "))
array1 = array('i', [])
for i in range(element):
    array1.append(int(input("Enter the element: ")))

delete = int(input("Enter an element to delete: "))

array1.remove(delete)

print(array1)