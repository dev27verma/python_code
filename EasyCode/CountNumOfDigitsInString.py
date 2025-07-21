import digit

def count_char(string):
    char = [i for i in string if i.isalpha()]
    return char

def count_digit(string):
    digit = [i for i in string if i.isdigit()]
    return digit

def remove_duplicate_char(duplicate):
    my_list = count_char(string)
    my_list1 = []
    for item in my_list:
        if item not in my_list1:
            my_list1.append(item)
    return my_list1

def remove_duplicate_digit(duplicate):
    my_list = count_digit(string)
    my_list1 = []
    for item in my_list:
        if item not in my_list1:
            my_list1.append(item)
    return my_list1

string = input("Enter a string: ")
# count with duplicate character and print string
print(f"Character in String: {count_char(string)}")
print(f"number of character in string: {len(count_char(string))}")
# count with duplicate digit and print digit
print(f"Numeric Values in string: {count_digit(string)}")
print(f"number of numeric value in string: {len(count_digit(string))}")
# count after duplicate character removed and print string
print(f"Character in String: {remove_duplicate_char(string)}")
print(f"number of character in string: {len(remove_duplicate_char(string))}")
# count after duplicate number removed and print number in string
print(f"Character in String: {remove_duplicate_digit(string)}")
print(f"number of character in string: {len(remove_duplicate_digit(string))}")