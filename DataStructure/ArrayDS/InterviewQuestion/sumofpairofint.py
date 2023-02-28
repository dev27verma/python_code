# Write a program to find all pairs of integers whose sum is equal to a given number?
"""
example solution in question
I/P [2,6,3,9,11] target sum 9 --->  O/p [6,3]

Question to ask to interviewers:
Does array contain only positive or negative numbers?
What if the same pair repeat twice, should we print it everytime?
If the reverse of the pair is acceptable eg can we print both [1,4] and [4,1], if given target is 5? --> not valid
Do we need to print only distinct pair? Does [3,3] is a valid pair for given target 6?       ---> not valid
How big is the array?
"""
import numpy as np

element = int(input("Enter the number of element required: "))
mat = []
for i in range(element):
    mat.append(int(input("Enter element: ")))
array1 = np.array(mat)
print(array1)

target = int(input("Target sum: "))


def sum_of_pair(arr, t):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == t:
                print(f"[{i, j}]", end=' ')


sum_of_pair(array1, target)
