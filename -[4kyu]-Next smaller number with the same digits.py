def next_smaller(n):
    def find_smaller(digits_left: list[str], number: str, pivot: str) -> list[int] | None:
        if number and int(number) > int(pivot[:len(number)]):
            return None
        if not digits_left:
            return [int(number)] if len(number) == len(pivot) and int(number) != int(pivot) else None
        candidates = []
        for digit in digits_left:
            digits_copy = digits_left.copy()
            digits_copy.remove(digit)
            candidate = find_smaller(digits_copy, number + digit, pivot)
            if candidate:
                candidates += candidate
        return candidates
    digits = [x for x in str(n)]
    smaller_than_n = find_smaller(digits, "", str(n))
    return max(smaller_than_n) if smaller_than_n else -1


print(next_smaller(100), 790)
