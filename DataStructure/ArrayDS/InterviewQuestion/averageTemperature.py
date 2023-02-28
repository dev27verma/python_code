import numpy as np

element = int(input("How many days Temperature is required: "))
mat = []
for i in range(element):
    mat.append(float(input(f"Day {i}: ")))
array1 = np.array(mat)

print(array1)


def average(arr):
    avg = round(sum(arr) / len(arr), 2)
    return avg


print(f"Average Temperature is: {average(array1)}")


def day_temp_above_average(arr):
    avg = average(arr)
    result = []
    count = 0
    for i in arr:
        if i > avg:
            count += 1
            result.append(i)
    print(f"{count}'Days are having above average Temperature\n Temperature above average are: {result}")


day_temp_above_average(array1)
