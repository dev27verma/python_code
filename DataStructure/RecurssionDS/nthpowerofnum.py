number = int(input("Enter a number: "))
power = int(input("Enter the power for a number: "))


def power_of_num(n, p):
    assert 0 <= p == int(p) or 0 <= n == int(n), 'Only Positive integer is allowed'
    if p == 0:
        return 1
    if p == 1:
        return n
    else:
        return n * power_of_num(n, p - 1)


print(f"{power_of_num(number, power)}")
