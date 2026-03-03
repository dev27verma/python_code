string = "string"
print(string[::-1])

str = ""
for i in string:
    str = i + str
print(str)





# given a string generate a new string consisting of its last two characters, reversed and seperated by a space


def transform_string(s):
    last_two = s[-2:]        # get last two characters
    reversed_two = last_two[::-1]   # reverse them
    return " ".join(reversed_two)   # separate by space

# Example
print(transform_string("hello world"))   # output should be d l
print(transform_string("I am the king"))   # output should be g n