string = input("Enter the string to check: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("not palindrome")