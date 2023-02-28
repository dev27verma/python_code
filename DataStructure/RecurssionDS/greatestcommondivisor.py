number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))


def gcd(num1, num2):
    assert num1 == int(num1) or num2 == int(num2), "Number must be integer"
    if num1 < 0:
        num1 *= -1
    if num2 < 0:
        num2 *= -1
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


print(f"Greatest Common Divisor of {number1} and {number2}: {gcd(number1, number2)}")
