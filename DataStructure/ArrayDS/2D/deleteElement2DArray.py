import numpy as np

ro = int(input("enter the number or row required: "))
col = int(input("Enter the number of column required: "))

mat = []

for i in range(ro):
    a = []
    for j in range(col):
        a.append(int(input(f"[{i}][{j}]: ")))
    mat.append(a)
matrix = np.array(mat)


def traverse(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
        print()


traverse(matrix)

delete_row = np.delete(matrix, 0 , axis=0)
print(delete_row)

delete_col = np.delete(matrix, 0 , axis=1)
print(delete_col)