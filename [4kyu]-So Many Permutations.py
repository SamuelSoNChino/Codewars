def permutations(s):
    perms = []

    def generate(perm: str, characters: dict):
        if not characters:
            if perm in perms:
                return
            else:
                perms.append(perm)
                return
        for char in characters.keys():
            new_characters = characters.copy()
            new_characters[char] -= 1
            if new_characters[char] == 0:
                new_characters.pop(char)
            generate(perm + char, new_characters)
        return

    chars = {}
    for char in s:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    generate("", chars)
    return perms


print(sorted(permutations('a')), ['a'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), [
      'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
