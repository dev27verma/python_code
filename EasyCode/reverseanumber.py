num = int(input("Enter the number: "))
rev = 0
while num != 0:
    rev = num % 10 + rev * 10
    num = num // 10

print(rev)
