def sum_of_intervals(intervals: list):
    summ = 0
    for interval in intervals:
        for interval2 in intervals:
            if interval in intervals and interval2 in intervals:
                if interval == interval2 and intervals.count(interval) != 1:
                    intervals.remove(interval2)
                elif interval[0] < interval2[0] < interval[1]:
                    intervals.append(
                        (interval[0], max(interval[1], interval2[1])))
                    intervals.remove(interval)
                    intervals.remove(interval2)
                elif interval[0] < interval2[1] < interval[1]:
                    intervals.append(
                        (min(interval[0], interval2[0]), interval[1]))
                    intervals.remove(interval)
                    intervals.remove(interval2)
    for interval in intervals:
        summ += len(range(interval[0], interval[1]))
    return summ


print(sum_of_intervals([(1, 5), (0, 6)]), 4)
print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
