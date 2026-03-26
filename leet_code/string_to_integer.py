def multiAtoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    i = 0
    n = len(s)
    result = []

    while i < n:
        # Skip non-digit & non-sign characters
        if not (s[i].isdigit() or s[i] in '+-'):
            i += 1
            continue

        # Handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # If sign not followed by digit → skip
        if i >= n or not s[i].isdigit():
            continue

        num = 0

        # Build number
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check
            if num > (INT_MAX - digit) // 10:
                num = INT_MAX if sign == 1 else INT_MIN
                break

            num = num * 10 + digit
            i += 1

        result.append(sign * num)

    return result


# 🔹 Dynamic Input
s = input("Enter a string: ")

# 🔹 Output
numbers = multiAtoi(s)
print("\nExtracted Numbers:", numbers)