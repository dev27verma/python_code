# Number of rows
rows = int(input("Number of rows to enter: "))
for i in range(rows):
    # print star in first and last row
    if i == 0 or i == rows - 1:
        print('*' * rows)
    else:
        # print * in first and last position in other rows
        print('*' + ' ' * (rows - 2) + '*')