def permutations(s):
    perms = []

    def generate(perm: str, characters: list):
        if not characters:
            if perm in perms:
                return
            else:
                perms.append(perm)
                return
        tried = []
        for char in characters:
            if char not in tried:
                tried.append(char)
                new_characters = characters.copy()
                new_characters.remove(char)
                generate(perm + char, new_characters)
        return
    
    generate("", [char for char in s])
    return perms

print(sorted(permutations('a')), ['a']);
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


            
        