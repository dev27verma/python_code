# Given an image represented by an NXN matrix, write a method to rotate the image by 90 degrees.
import numpy as np

ro = int(input("Enter the rows: "))
col = int(input("Enter the column: "))
mat = []
for i in range(ro):
    a = []
    for j in range(col):
        a.append(int(input(f"[{i}][{j}]: ")))
    mat.append(a)
my_array = np.array(mat)

print(my_array)
print()


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]  # save top
            matrix[layer][i] = matrix[-i - 1][layer]  # left -> top
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]  # bottom -> left
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]  # right -> bottom
            matrix[i][- layer - 1] = top  # top -> right
    return matrix


print(rotate_matrix(my_array))
