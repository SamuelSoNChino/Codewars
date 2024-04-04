import math


def decompose(rem, sol=[]):
    if rem == 0:
        return sol
    if rem < 0:
        return None

    if sol:
        max = int(math.sqrt(rem))
    else:
        rem = rem ** 2
        max = int(math.sqrt(rem)) - 1

    for i in range(max, 0, -1):
        if sol:
            if i < sol[-1]:
                res = decompose(rem - i ** 2, sol + [i])
                if res:
                    return res
        else:
            res = decompose(rem - i ** 2, sol + [i])
            if res:
                return res[::-1]
    return None


print(decompose(5))
print(decompose(50))
