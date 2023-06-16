string = input("Enter a string: ")
char = [i for i in string if i.isalpha()]
print(char)
print(f"number of character in string: {len(char)}")

digit = [i for i in string if i.isdigit()]
print(digit)
print(f"number of numeric value in string: {len(digit)}")