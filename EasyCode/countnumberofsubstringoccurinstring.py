def frequency_of_substring(s, sub):
    count = 0
    for i in range(len(s)):
        if string[i:].startswith(sub):
            count += 1
    return count


string = input("Enter a string: ")
sub_string = input("Enter a sub string: ")
print(frequency_of_substring(string, sub_string))
