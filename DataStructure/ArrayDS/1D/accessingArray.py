from array import *

arr1 = array('i', [1, 2, 3, 4, 5])


def accessing_array(arr, index):
    if index >= len(arr):
        print('Index Not Found')
    else:
        print(arr[index])


accessing_array(arr1, 2)
