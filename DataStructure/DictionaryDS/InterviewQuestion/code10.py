# Q-10. What will be the output of the following code snippet?

rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id1 = id(rec)
del rec
rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id2 = id(rec)
print(id1 == id2)

# A. True
# B. False
# C. 1
# D. Exception
