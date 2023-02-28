num = int(input("Enter the list len"))
list = []
for i in range(1,num):
    list.append(input("Insert Element: "))

print(f"first Element: {list[0]}")
print(f"last element {list[i-1]}")
print("\n")
list[0],list[i-1] = list[i-1],list[0]

print(f"first Element: {list[0]}")
print(f"last element {list[i-1]}")