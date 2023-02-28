num = int(input("Enter the number: "))


def factorial(n):
    assert n >= 0, 'only positive integer allowed'
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(num))

'''
O(n) -- answer is in copy
'''