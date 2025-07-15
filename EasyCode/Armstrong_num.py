# find the sum of the cube of each digit
def arm_strong(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10
    return sum


num = int(input("Enter a number: "))
# display the result
if num == arm_strong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
