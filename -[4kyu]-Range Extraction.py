def solution(args):
    res = ""
    last = args[0]
    range = [last]
    for num in args[1:-1]:
        if num == last + 1:
            range.append(num)
        elif len(range) < 3:
            for num2 in range:
                res += str(num2) + ","
            range = [num]
        else:
            res += str(range[0]) + "-" + str(range[-1]) + ","
            range = [num]
        last = num
    if args[-1] == last + 1:
        res += str(range[0]) + "-" + str(args[-1])
    elif len(range) < 3:
        for num2 in range:
            res += str(num2) + ","
        res += str(args[-1])
    else:
        res += str(range[0]) + "-" + str(range[-1]) + ","
        res += str(args[-1])
    return res


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11,
      14, 15, 17, 18, 19, 20]) + "\n" + '-6,-3-1,3-5,7-11,14,15,17-20')
