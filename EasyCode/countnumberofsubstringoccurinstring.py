string = input("Enter a string: ")
sub_string = input("Enter a sub string: ")


def frequency_of_substring(s, sub):
    count = 0
    for i in range(len(s)):
        if string[i:].startswith(sub):
            count += 1
    return count


print(frequency_of_substring(string, sub_string))



'''METHOD 2'''


string, substring = (input("Enter a string: ").strip(), input("Enter a sub string: ").strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))