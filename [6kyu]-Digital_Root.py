def digital_root(n):
    while n >= 10:
        m = sum([int(x) for x in str(n)])
        n = m
    return n

print(digital_root(16))