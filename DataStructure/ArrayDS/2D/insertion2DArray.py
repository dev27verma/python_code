import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

new_arr_insert_column = np.insert(arr, 0, [[2, 3, 4]], axis=1)
print(new_arr_insert_column)


new_arr_insert_row = np.insert(arr, 0, [[2, 3, 4]], axis=0)
print(new_arr_insert_row)