num = int(input("Enter the num: "))
palindrome = 0
temp = num

while num > 0:
    rem = num % 10
    palindrome = palindrome * 10 + rem
    num =  num // 10

if palindrome == temp:
    print(f"{palindrome} is palindrome")
else:
    print(f"{palindrome} is not palindrome")

'''Palindrome of string'''
string = input("Enter a string: ")
temp = string[::-1]
if string == temp:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")

