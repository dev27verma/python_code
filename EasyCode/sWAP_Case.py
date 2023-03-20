string = input("Enter a String to swap upper char to lower and lower char to upper: ")


def swap_case(s):
    temp = ""
    for i in s:
        if i.isupper():
            temp += i.lower()
        else:
            temp += i.upper()
    return temp


print(swap_case(string))



