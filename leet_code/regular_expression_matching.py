def isMatch(s, p):
    m, n = len(s), len(p)

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, etc.
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # Case 1: direct match or '.'
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]

            # Case 2: '*'
            elif p[j - 1] == '*':
                # Ignore previous char + '*'
                dp[i][j] = dp[i][j - 2]

                # Use '*' if match
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] |= dp[i - 1][j]

    return dp[m][n]


# 🔹 Dynamic Input
s = input("Enter string: ")
p = input("Enter pattern: ")

# 🔹 Output
print("\nMatch Result:", isMatch(s, p))