def count_string_word(s):
    words = s.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result

s = input("Enter a sentence: ")
print(count_string_word(s))


# --------------------------------------------
# Using function

def count_string_words(s):
    result = {word: len(word) for word in s.split()}
    return result

print(count_string_words(s))