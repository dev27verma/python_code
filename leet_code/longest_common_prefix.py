def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# 🔹 Dynamic Input
n = int(input("Enter number of strings: "))
print("Enter strings:")

strs = []
for _ in range(n):
    strs.append(input())

# 🔹 Output
result = longestCommonPrefix(strs)
print("\nLongest Common Prefix:", result)