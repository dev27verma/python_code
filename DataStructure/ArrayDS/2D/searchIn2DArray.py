import numpy as np

ro = int(input("Enter the number of row required: "))
col = int(input("Enter the number of column required: "))

mat = []
for i in range(ro):
    a = []
    for j in range(col):
        a.append(int(input(f"[{i}][{j}]: ")))
    mat.append(a)
matrix = np.array(mat)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()

val = int(input("Enter the value which you want to search: "))


def search(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return "value found at row: " + str(i + 1) + " " + "column: " + str(j + 1)
    return "Value not found"


print(search(matrix, val))
