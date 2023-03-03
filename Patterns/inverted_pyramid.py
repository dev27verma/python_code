# Number of rows
rows = int(input("Number of rows to enter: "))
for star in range(0, rows):
    for i in range(rows, star , -1):
        print("*", end=" ")
    print()