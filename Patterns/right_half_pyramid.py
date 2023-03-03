# Number of rows
rows = int(input("Number of rows to enter: "))
# Loop through rows
for star in range(rows):
    # Loop to print the stars
    for i in range(star):
        print("*", end=" ")
    print()
