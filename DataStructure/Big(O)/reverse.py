element = int(input("Enter number of element to be enter in array: "))
array = []
for index in range(element):
    array.append(int(input("Enter the element: ")))


def reverse(arr):
    for i in range(int(len(arr) / 2)):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    print(arr)


reverse(array)


'''
8. O(n/2) --> removing constant will be O(n)
9,10,11,12,13 --> all are assignment so it will be O(1)

Time Complexity - O(n)
'''