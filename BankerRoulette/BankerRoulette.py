import random

name = input("Give Everybody's name ").split(',')

# choose = random.choice(name)   --- second way in this after the current line only print is required

length_of_list = len(name)
random_person = random.randint(0, length_of_list - 1)
person_who_will_pay = name[random_person]

print(person_who_will_pay + " is going to pay for party")
