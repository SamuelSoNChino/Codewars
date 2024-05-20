def mix(s1: str, s2: str):
    char_dict = {}
    for char in s1:
        if char.islower() and char not in char_dict.keys():
            char_dict[char] = [1, 0]
        elif char.islower():
            char_dict[char][0] += 1

    for char in s2:
        if char.islower() and char not in char_dict.keys():
            char_dict[char] = [0, 1]
        elif char.islower():
            char_dict[char][1] += 1

    char_dict = dict(
        sorted(char_dict.items(), key=lambda item: max(item[1]), reverse=True))
    output = ""
    for char in char_dict.keys():
        maximum = max(char_dict[char])
        if maximum == 1:
            break
        if char_dict[char].count(maximum) == 2:
            output += f'=:{maximum * char}/'
        else:
            ()
            output += f'{char_dict[char].index(maximum) + 1}:{maximum * char}/'
    return output[:-1]


print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
      '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
print(mix("looping is fun but dangerous", "less dangerous than coding"),
      "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
print(mix(" In many languages", " there's a pair of functions"),
      "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
print(mix("codewars", "codewars"), "")
print(mix("A generation must confront the looming ", "codewarrs"),
      "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
