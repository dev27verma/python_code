def even_sum(num):
    sum = 0
    for i in range(2, num, 2):
        sum += i
    return sum


def odd_sum(num):
    sum = 0
    for i in range(1, num, 2):
        sum += i
    return sum


num = int(input("Enter the number till which we want even or odd sum? "))

print(f"Sum of even number is: {even_sum(num)}")
print(f"Sum of odd number is {odd_sum(num)}")
