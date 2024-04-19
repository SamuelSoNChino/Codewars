def middle_permutation(string):
    letters = sorted([letter for letter in string])
    if len(letters) % 2 == 0:
        result = letters.pop(len(letters) // 2 - 1)
        for _ in range(len(letters)):
            result += letters.pop(-1)
    else:
        result = ""
        index = 0
        result = letters.pop(len(letters) // 2)
        result += letters.pop(len(letters) // 2 - 1)
        for _ in range(len(letters)):
            result += letters.pop(-1)
    return result


print(middle_permutation("abc"), "bac")
print(middle_permutation("abcd"), "bdca")
print(middle_permutation("abcdx"), "cbxda")
print(middle_permutation("abcdxg"), "cxgdba")
print(middle_permutation("abcdxgz"), "dczxgba")

