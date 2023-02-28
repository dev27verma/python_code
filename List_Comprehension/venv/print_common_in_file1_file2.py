import pandas

with open("file1.txt") as file_1:
    file1 = file_1.readlines()

with open("file2.txt") as file_2:
    file2 = file_2.read()

result = [int(num) for num in file1 if num in file2]
print(result)
