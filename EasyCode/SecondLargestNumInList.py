num = int(input("Enter number of string: "))
arr = []
for i in range(num):
    arr.append(int(input("Enter the values: ")))

arr = [arr[i] for i in range(len(arr) - 1) if arr[i] < arr[i + 1]]
print(arr[-1])
