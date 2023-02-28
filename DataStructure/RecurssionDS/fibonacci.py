num = int(input("Enter a num: "))


def fibonacci(n):
    assert 0 <= n == int(n), 'Only positive integer allowed'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(num))
