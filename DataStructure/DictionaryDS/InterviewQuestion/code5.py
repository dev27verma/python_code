# Q-5. What will be the output of the following code snippet?

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)

# A. 7
# B. Syntax error
# C. 3
# D. 6
