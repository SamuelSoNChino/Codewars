def prime_factors(n):
    res = ""
    i = 2
    while n != 1:
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count == 1:
            res += f'({str(i)})'
        elif count:
            res += f'({str(i)}**{str(count)})'
        i += 1
    return res


print(prime_factors(60), "(2**2)(3**3)(5)(7)(11**2)(17)")
