num = int(input("Enter a number: "))


def factorial(n):
    assert 0 <= n == int(n), 'The number must be positive integer only'       # n >=0 and int(n) == n
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(f"factorial of {num}: {factorial(num)}")
