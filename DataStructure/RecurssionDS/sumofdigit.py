num = int(input("Enter a number: "))


def sum_of_digit(n):
    assert 0 <= n == int(n), 'Only positive integer is allowed'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digit(n // 10)


print(f"sum of individual digit of {num}: {sum_of_digit(num)}")
