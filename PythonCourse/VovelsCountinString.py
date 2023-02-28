string = input("Enter a string: ").lower()
vovel = 0
for i in string:
    if i == 'a' or i == "e" or i == "i" or i == "o" or i == "u":
        vovel += 1
print(vovel)