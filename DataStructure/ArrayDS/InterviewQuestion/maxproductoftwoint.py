#   How to find maximum product of two integers in the array where all elements are positive

import numpy as np

element = int(input("Enter the number of element required: "))
my_list = []
for i in range(element):
    my_list.append(int(input("Enter value: ")))
array1 = np.array(my_list)


def find_max_product(arr):
    product = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > product:
                product = arr[i] * arr[j]
                pairs = str(arr[i]) + "," + str(arr[j])
    print(f"Pair of two largest numbers: {pairs}")
    print(f"Product of {pairs}: {product}")


find_max_product(array1)
