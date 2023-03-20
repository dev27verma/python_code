# 🚨 Don't change the code below 👇
number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

result = 0
for i in range(len(number)):
    num = int(number[i])
    result += num
print(result)