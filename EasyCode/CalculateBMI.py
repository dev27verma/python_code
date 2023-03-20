'''
Calculate BMi and give O/P on integer
'''

weight = input("Enter weight: ")
height = input("Enter height ")

bmi = int((float(weight) / (((float(height)/100) ** 2))))
print(bmi)