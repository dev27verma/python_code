# Permutation: len and list should be same for two list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 2, 5, 1]


def permutation(l1, l2):
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False


print(permutation(list1, list2))
