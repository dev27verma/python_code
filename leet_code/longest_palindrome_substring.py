def longestPalindrome(s):
    if not s:
        return ""

    start, end = 0, 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd length
        l1, r1 = expand(i, i)
        # Even length
        l2, r2 = expand(i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1

        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


# 🔹 Dynamic Input
s = input("Enter a string: ")

# 🔹 Output
result = longestPalindrome(s)
print("\nLongest Palindromic Substring:", result)
print("Length:", len(result))