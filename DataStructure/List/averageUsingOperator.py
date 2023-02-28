my_list = []
while True:
    num = input("Enter a num: ")
    if num == 'done':
        break
    my_list.append(float(num))
average = sum(my_list) / len(my_list)
print(f"Average: {average}")
