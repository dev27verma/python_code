def changeAds(base10: int) -> int:
    # Convert to binary and strip the '0b' prefix
    binary_str = bin(base10)[2:]

    # Flip the bits
    flipped = ''.join('0' if bit == '1' else '1' for bit in binary_str)

    # Convert back to base 10
    return int(flipped, 2)


# Take input from user
try:
    num = int(input("Enter an integer (base 10): "))
    result = changeAds(num)
    print("Resulting integer after flipping:", result)
except ValueError:
    print("Please enter a valid integer.")
