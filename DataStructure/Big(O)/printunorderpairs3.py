elementA = int(input("Enter number of element to be enter in array: "))
arrA = []
for index in range(elementA):
    arrA.append(int(input("Enter the element: ")))

elementB = int(input("Enter number of element to be enter in array: "))
arrB = []
for index in range(elementB):
    arrB.append(int(input("Enter the element: ")))


def print_unorder_array(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))


print_unorder_array(arrA, arrB)


'''
13. O(A) 14. O(B) 15. 0(100000) 16. 0(1)

Time Complexity: O(AB)

Since there are two array, and each loop is running for different array, so it will not be 'n2' but it should be a multiple of two array.
O(100000) is constant so we can write it as O(1) or ignore.
'''