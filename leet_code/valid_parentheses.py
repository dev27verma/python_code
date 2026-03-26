def isValid(s):
    stack = []

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping.values():  # opening
            stack.append(char)
        elif char in mapping:  # closing
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


# 🔹 Dynamic Input
s = input("Enter parentheses string: ")

# 🔹 Output
if isValid(s):
    print("\nValid Parentheses ✅")
else:
    print("\nInvalid Parentheses ❌")