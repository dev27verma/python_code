def intToRoman(num):
    val_map = [
        (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I")
    ]

    result = ""
    for val, symbol in val_map:
        while num >= val:
            result += symbol
            num -= val
    return result


def romanToInt(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]

    return total


# 🔁 Continuous Loop
while True:
    print("\n--- Roman Converter ---")
    print("1. Integer → Roman")
    print("2. Roman → Integer")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        num = int(input("Enter integer: "))
        print("Roman:", intToRoman(num))

    elif choice == '2':
        s = input("Enter Roman numeral: ")
        print("Integer:", romanToInt(s))

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")