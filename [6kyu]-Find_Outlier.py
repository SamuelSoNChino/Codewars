def find_outlier(integers):
    sum = 0
    remain = None
    for integer in integers[:3]:
        sum += integer % 2
    remain = 1 if sum >= 2 else 0
    for integer in integers:
        if integer % 2 != remain:
            return integer
