element = int(input("Enter number of element to be enter in array: "))
array = []
for index in range(element):
    array.append(int(input("Enter the element: ")))


def print_unordered_paris(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f'{arr[i]},{arr[j]}')


print_unordered_paris(array)
