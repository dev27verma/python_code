n = int(input("Enter number of element to enter: "))
array = []

for i in range(n):
    array.append(int(input("Enter integer: ")))


def product_of_array(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product_of_array(arr[1:])


print(f"Result of product of all element of array: {product_of_array(array)}")
