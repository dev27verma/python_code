# Q-3. What will be the output of the following code block?

fruit = {}


def add_one(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1


add_one('Apple')
add_one('Banana')
add_one('apple')
print(len(fruit))

# A. 1
# B. 2
# C. 3
# D. 4
