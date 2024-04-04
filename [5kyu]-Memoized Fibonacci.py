def fibonacci(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if n in [0, 1]:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return fibonacci(n - 1, memo) + fibonacci(n - 2, memo)


print(fibonacci(50))
