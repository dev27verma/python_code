#############################
#        Star Pattern       #
#############################
# Number of rows
rows = int(input("Number of rows to enter: "))
# Loop through rows
for star in range(rows):
    # Loop to print the stars
    for i in range(star):
        print("*", end=" ")
    print()


#############################
#    number pattern         #
#############################

# Loop through rows
for star in range(rows):
    # Loop to print the stars
    for i in range(star):
        print(star, end=" ")
    print()
#############################
#    number pattern +1      #
#############################

for star in range(1, rows + 1):
    # Loop to print the stars
    for i in range(1, star + 1):
        print(i, end=" ")
    print()