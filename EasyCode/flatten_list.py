# x = [1, [2, [3,4],5], 6]
# output [1,2,3,4,5,6]

import ast

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

# Take input from user
user_input = input("Enter a nested list (e.g., [1, [2, [3,4],5], 6]): ")

# Convert string input to actual list
x = ast.literal_eval(user_input)

print("Flattened list:", flatten(x))

