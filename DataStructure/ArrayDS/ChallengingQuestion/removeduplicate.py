element = int(input("Enter the number of element required: "))
my_list = []
for i in range(element):
    my_list.append(int(input("Enter Element: ")))
print(my_list)


def remove_duplicate(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


print("After removing duplicate value")
print(remove_duplicate(my_list))
