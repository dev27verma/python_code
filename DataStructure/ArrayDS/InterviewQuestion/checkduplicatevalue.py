# IS Unique: Implement an algo to determine if a list has all unique character, using python list

element = int(input("Enter the number of element required: "))
my_list1 = []
for i in range(element):
    my_list1.append(int(input("Enter element: ")))
print(my_list1)


def is_unique(my_list):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                return False
    return True


print(is_unique(my_list1))
