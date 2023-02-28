def getSum(number):
    sum = 0
    while (number != 0):
        sum = sum + (number % 10)
        number = number // 10

    return sum


num = int(input("Enter the number? "))
print(getSum(num))
