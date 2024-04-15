def is_interesting(number, awesome_phrases):
    for i in range(3):
        num = number + i
        if num > 99:
            res_val = 2 if i == 0 else 1
            for awesome_phrase in awesome_phrases:
                if num == awesome_phrase:
                    return res_val
            if str(num) == str(num)[::-1]:
                return res_val
            non_zeros = 0
            increasing = True
            decreasing = True
            last_digit = -1
            for digit in str(num):
                if digit != "0":
                    non_zeros += 1
                if digit != str(last_digit + 1)[-1] and last_digit != -1:
                    increasing = False
                if digit != str(last_digit - 1)[-1] and last_digit != -1:
                    decreasing = False
                last_digit = int(digit)
            if increasing or decreasing or non_zeros == 1:
                return res_val
    return 0


print(is_interesting(1336, [1337, 256]))
