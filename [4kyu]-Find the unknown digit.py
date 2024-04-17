def solve_runes(runes: str):
    possible_digits = [chr(x) for x in range(ord("0"), ord("9") + 1)]
    operator = ""
    operator_index = -1
    first_num = ""
    second_num = ""
    result = ""
    if runes[0] == "?" or runes[0] == "-" and runes[1] == "0":
        possible_digits.pop(possible_digits.index("0"))
    for i, char in enumerate(runes):
        if not operator and char in "+-*" and i != 0:
            operator = char
            operator_index = i
        if char == "=":
            first_num = runes[:operator_index]
            second_num = runes[operator_index + 1:i]
            result = runes[i + 1:]
        if char in possible_digits:
            possible_digits.pop(possible_digits.index(char))
    for char in possible_digits:
        if operator == "*":
            if int(first_num.replace("?", char)) * int(second_num.replace("?", char)) == int(result.replace("?", char)):
                return int(char)
        elif operator == "-":
            if int(first_num.replace("?", char)) - int(second_num.replace("?", char)) == int(result.replace("?", char)):
                return int(char)
        else:
            if int(first_num.replace("?", char)) + int(second_num.replace("?", char)) == int(result.replace("?", char)):
                return int(char)
    return -1


print(solve_runes("1+1=?"), 2, "Answer for runes = '1+1=?' ")
