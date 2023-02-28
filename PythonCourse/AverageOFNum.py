num = int(input("Enter numbers to be entered: "))
number = []
for n in range(num):
    elements = int(input("Enter Elements: "))
    number.append(elements)

average = sum(number)/num
print("average is: ", average)