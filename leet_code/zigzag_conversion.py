def zigzagConvert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    current_row = 0
    direction = -1  # will switch between down/up

    for char in s:
        rows[current_row] += char

        # Change direction at top/bottom
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1

        current_row += direction

    return "".join(rows)


# 🔹 Dynamic Input
s = input("Enter string: ")
numRows = int(input("Enter number of rows: "))

# 🔹 Output
result = zigzagConvert(s, numRows)
print("\nZigzag Conversion:", result)