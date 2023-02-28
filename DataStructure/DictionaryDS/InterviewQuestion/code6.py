# Q-6. What will be the output of the following code snippet?

my_dict = {}
my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)

# A. Syntax error
# B. 30
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# C. 47
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# D. 30
#     {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}
