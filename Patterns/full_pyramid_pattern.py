rows = int(input("Enter rows: "))
for star in range(0, rows):
    for i in range(0, rows - star -1):
        print(end=" ")
    for i in range(0, star + 1):
        print("*", end=" ")
    print()