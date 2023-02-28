word = input("Enter a string: ")


def reverse(string):
    assert len(string) >= 1, "Length of string should be atleast 1"
    if len(string) == 1:
        return string
    return string[-1] + reverse(string[0:-1])


print(f"Reverse of string: {reverse(word)}")
