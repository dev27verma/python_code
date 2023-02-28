element = int(input("Enter number of element to be enter in array: "))
arr = []
for index in range(element):
    arr.append(int(input("Enter the element: ")))


def calculate(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print(f"Sum of element of array: {sum}\nProduct of element of array: {product}")


calculate(arr)

'''
-----------
We need to find Big O of the code
1. 0(1) 2. 0(1) 3. O(N) 4. O(1)
8. O(1) 9. O(1) 10. O(N)
11. 0(1) 12. O(N) 13. O(1)
14. O(1)

O/P Time Complexity -- O(n)
-----------
'''
