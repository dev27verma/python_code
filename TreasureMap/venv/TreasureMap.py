# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row4 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row5 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row6 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row7 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]
row8 = ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]

map = [row1, row2, row3, row4, row5, row6, row7, row8]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = 'X'
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")