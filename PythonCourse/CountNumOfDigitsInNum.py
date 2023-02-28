string = input("Enter a string: ")
arr = [i for i in string if i.isalpha()]
print(arr)

count = 0
for i in string:
    if i.isalpha():
        count +=1
        print(i, end="")
print()
print(f"number of character in string: {count}")

print("\n")

number=0
for i in string:
    if i.isdigit():
        number += 1
        print(i, end="")
print()
print(f"number of numeric value in string: {number}")