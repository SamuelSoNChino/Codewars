def format_duration(seconds):
    if seconds == 0:
        return "now"
    dic = {"year": (365 * 24 * 3600),
           "day": (24 * 3600),
           "hour": 3600,
           "minute": 60,
           "second": 1}
    result = ""
    last = ""
    for comp in dic.keys():
        num = seconds // dic[comp]
        if num != 0:
            seconds %= dic[comp]
            if last:
                result += last
                last = f', {num} {comp}{"s" if num > 1 else ""}'
            else:
                last = f'{num} {comp}{"s" if num > 1 else ""}'
    if result:
        result += " and " + last[2:]
    else:
        return last
    return result


print(format_duration(33243586))
