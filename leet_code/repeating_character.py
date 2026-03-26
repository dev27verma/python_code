'''Longest substring without repeating character

Enter a string: pwwkew
Length: 3
Substring: wke

Enter a string: abcabcbb
Length: 3
Substring: abc
'''
def longestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    start = 0  # to track substring start

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

    return max_length, s[start:start + max_length]


# 🔹 Dynamic Input
s = input("Enter a string: ")

length, substring = longestSubstring(s)

# 🔹 Output
print("\nLongest Substring Without Repeating Characters:")
print("Length:", length)
print("Substring:", substring)