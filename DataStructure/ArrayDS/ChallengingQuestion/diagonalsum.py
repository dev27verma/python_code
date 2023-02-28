import numpy as np

ro = int(input("Enter the number of row required: "))
col = int(input("Enter the number of column required: "))

mat = []
for i in range(ro):
    ar = []
    for j in range(col):
        ar.append(int(input(f"[{i}][{j}]: ")))
    mat.append(ar)
my_array = np.array(mat)
print(my_array)


def sum_diagonal(arr):
    sum = 0
    for a in range(len(arr)):
        sum += arr[a][a]
    return sum


print(f"Sum of diagonals: {sum_diagonal(my_array)}")
