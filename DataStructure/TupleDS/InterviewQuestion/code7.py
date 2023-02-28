# Q-7. What will be the output of the following code block?

my_list = [1, 2, 3]
init_tuple = ('Python',) * (my_list.__len__() - my_list[::-1][0])

print(init_tuple)

# A. ()
# B. (‘Python’)
# C. (‘Python’, ‘Python’)
# D. Runtime Exception.
