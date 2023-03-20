string = input("Enter a string: ").lower()

out = {x: string.count(x) for x in string}
print(out)

'''Second method'''


def frequency(text):
    for i in range(len(text)):
        if len(text) == 0:
            break
        ch = text[0]
        if ch == ' ' or ch == '\t':
            continue
        count = 1
        for j in range(1, len(text)):
            if ch == text[j]:
                count += 1
        text = text.replace(ch, ' ').strip()
        print(f"{ch} -> {count}")


frequency(string)
