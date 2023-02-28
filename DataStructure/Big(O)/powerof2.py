power = int(input("Enter the power: "))


def power_of_2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = power_of_2(int(n / 2))
        curr = prev * 2
        print(curr)
        return curr


print(power_of_2(power))

'''
Time Complexity: O(logN)
check notes
'''
