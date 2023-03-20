import math

print("Welcome to the tipe calculator")
total_bill = float(input("What was the total bill? "))
tip_percent = float(input("What percentage of tip would you like to give? 10, 12 or 15? "))
num_of_person = int(input("How many people to split the bill? "))

split_bill = (total_bill + (tip_percent / 100 * total_bill)) / num_of_person
print(f"Each person should pay: {round(split_bill,2)}")