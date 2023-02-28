element = int(input("Enter the number of element required: "))
my_list1 = []
for i in range(element):
    my_list1.append(int(input("Enter element: ")))
print(my_list1)

val = int(input("Enter the value to search: "))
# Method 1 IN Operator
if val in my_list1:
    print(f"Value of Index is: {my_list1.index(val)}")
else:
    print("Value not found")


# Method 2: Linear Search

def search(my_list, value):
    for i in my_list:
        if i == val:
            return my_list.index(val)
    return 'Value not present'


print(f"Value found at index: {search(my_list1, val)}")
