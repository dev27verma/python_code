def getSum(number):
    sum = 0
    while number != 0:
        sum = sum + (number % 10)
        number = number // 10

    return sum


num = int(input("Enter the number? "))
print(f"result of Method 1 is: {getSum(num)}")


# Method 2

def getSum(number):
    sum = 1
    for i in number:
        sum = int(i) + sum
    return sum


num = input("Enter the number? ")
print(f"Result of Method 2 is: {getSum(num)}")
