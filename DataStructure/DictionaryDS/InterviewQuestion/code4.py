# Q-4. What will be the output of the following code block?

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print(sum)

# A. 1
# B. 2
# C. 3
# D. 4
