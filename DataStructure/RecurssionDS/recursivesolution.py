# print true if there is any Odd number in the list

number = int(input("Enter the number of element to enter: "))
my_list = []
for i in range(number):
    my_list.append(int(input("Enter the number: ")))


def some_recursive(arr, odd):
    if len(arr) == 0:
        return False
    if not (odd(arr[0])):
        return some_recursive(arr[1:], odd)
    return True


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(f"Is there any odd number in the list: {some_recursive(my_list, is_odd)}")
