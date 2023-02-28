# Q-9. What will be the output of the following code snippet?

# id() - it takes one argument, and its unique.

rec = {"Name": "Python", "Age": "20"}
r = rec.copy()
print(id(r) == id(rec))
print(r == rec)

# A. True
# B. False
# C. 0
# D. 1
