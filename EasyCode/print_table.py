num = int(input("Enter the number for which table is needed? "))
till_num = int(input("Till which number you want the table? "))
for i in range(1, till_num + 1):
    print(f"{num} X {i}  = {i * num}")