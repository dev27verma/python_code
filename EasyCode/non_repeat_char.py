'''find first non repeating char

input swiss
output w

'''

from collections import Counter

#s = "swiss"

s = input("Enter the string: ")

freq = Counter(s)

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break