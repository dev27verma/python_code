# Number of rows
rows = 18
# Iterating value for column
k = 2 * rows - 2
# Loop through rows
for i in range(rows):
    # Loop to print initial spaces
    for j in range(k):
        print(end=" ")
    # Updating value of K
    k = k - 2
    # Loop to print the stars
    for j in range(i + 1):
        print("*", end=" ")
    print()