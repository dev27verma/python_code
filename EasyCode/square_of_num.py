# Write a Python function that generates a list of squares of numbers from 1 to n (inclusive).
# Provide an example call to this function with n=5.

def square_of_num(num):
    result = [i**2 for i in range(1, num+1)]
    return result

num = int(input("Enter a number: "))
print(square_of_num(num))