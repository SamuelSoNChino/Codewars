def narcissistic(value):
    exp = len(str(value))
    tar = 0
    for digit in str(value):
        tar += int(digit) ** exp
    return tar == value
