element = int(input("Enter the number of element to insert: "))
arr = []
for i in range(element):
    arr.append(int(input("Enter element: ")))


def biggest_number(array):
    big = array[0]
    for i in range(1, len(array)):
        if array[i] > big:
            big = arr[i]
    return big


print(f"Largest number is list: {biggest_number(arr)}")
