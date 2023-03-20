num = int(input("Enter the number: "))

add = 0

while num > 0:
    rem = num % 10
    add = add + rem
    num =  num // 10

print(add)