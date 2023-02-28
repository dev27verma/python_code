n = int(input("Enter the element to enter: "))


def recursive_range(num):
    assert 0 <= num == int(num), "num not allowed"
    if num == 0:
        return 0
    else:
        return num + recursive_range(num - 1)


print(f"Sum of element: {recursive_range(n)}")
