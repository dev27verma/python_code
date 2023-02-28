# Given a list find the best and second best score from list

my_list = [84, 85, 90, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]


def first_second(lst):
    lst.sort(reverse=True)
    print(lst)
    first = lst[0]
    second = 0
    for element in lst:
        if element != first:
            second = element
            return first, second


print(first_second(my_list))
