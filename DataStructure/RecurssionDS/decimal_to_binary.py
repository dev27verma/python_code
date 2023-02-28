number = int(input("Enter a Decimal Number: "))


def decimal_to_binary(n):
    assert int(n) == n, 'Only Integer allowed'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n // 2))


print(f"Binary of the {number}: {decimal_to_binary(number)}")
