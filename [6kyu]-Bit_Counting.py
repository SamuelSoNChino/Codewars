def count_bits(n):
    output = 0
    while n != 0:
        output += n % 2
        n //= 2
    return output