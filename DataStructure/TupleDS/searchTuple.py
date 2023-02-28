my_tuple = ('a', 'b', 'c', 'd', 'e')

e = input("Enter the element to search: ")


def search(tuple1, element):
    for i in tuple1:
        if i == element:
            return tuple1.index(i)
    return "Element not found"


print(f"Index of element {e}: {search(my_tuple, e)}")
