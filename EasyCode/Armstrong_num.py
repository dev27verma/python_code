# find the sum of the cube of each digit
def arm_strong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum


num = int(input("Enter a number: "))
# display the result
if num == arm_strong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
