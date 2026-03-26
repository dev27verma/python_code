'''
keypad mobile phone combinations
'''
def letterCombinations(digits):
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, path):
        # Base case
        if index == len(digits):
            result.append(path)
            return

        # Get letters for current digit
        letters = phone_map[digits[index]]

        for char in letters:
            backtrack(index + 1, path + char)

    backtrack(0, "")
    return result


# 🔹 Dynamic Input
digits = input("Enter digits (2-9): ")

# 🔹 Output
combinations = letterCombinations(digits)
print("\nCombinations:", combinations)
print("Total Count:", len(combinations))