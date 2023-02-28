my_list = int(input("Enter the number of element to enter: "))

arr = []
for i in range(my_list):
    arr.append(input("Enter the element: "))


def remove_duplicate(arr1):
    result = []
    [result.append(i) for i in arr1 if i not in result]
    return result


print(remove_duplicate(arr))
