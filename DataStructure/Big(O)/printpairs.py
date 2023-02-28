element = int(input("Enter number of element to be enter in array: "))
array = []
for index in range(element):
    array.append(int(input("Enter the element: ")))


def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(str(i) + "," + str(j))


print_pairs(array)

'''
-------------------------
1. O(1)  2. O(1)  3. O(N) 4. 0(1)
8. O(N2) 9. O(N) 10. O(1)

Time Complexity:- O(n2)
-------------------------
'''