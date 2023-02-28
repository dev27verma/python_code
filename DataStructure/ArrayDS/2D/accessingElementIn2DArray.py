import numpy as np

ro = int(input("Enter number of row required: "))
col = int(input("Enter number of column required: "))

mat = []

for i in range(ro):
    a = []
    for j in range(col):
        a.append(int(input(f"[{i}][{j}]: ")))
    mat.append(a)
matrix = np.array(mat)

for i in range(ro):
    for j in range(col):
        print(matrix[i][j], end=' ')
    print()

row_value = int(input("Enter the row which value you want: "))
col_value = int(input("Enter the column which value you want: "))


def accessing_element(arr, row, column):
    if row >= len(arr) or column >= len(arr[0]):  # 0 represent column
        print("Invalid row or Column number")
    else:
        print(f"Value found at index: {arr[row][column]}")


accessing_element(matrix, row_value, col_value)
