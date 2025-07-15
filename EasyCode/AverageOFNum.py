def average_number(num):
    for n in range(len(num)):
        num[n] = int(num[n])
    return num


num = input("Enter the numbers: ").split(',')
print(f"average of Numbers: {round(sum(average_number(num)) // len(average_number(num)))}")
