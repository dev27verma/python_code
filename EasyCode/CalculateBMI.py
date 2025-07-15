'''
Calculate BMi and give O/P on integer
'''

weight = input("Enter weight in KG: ")
height = input("Enter height in cm: ")

bmi = float((float(weight) / ((float(height) / 100) ** 2)))
print(f"Your BMI is {bmi}")
