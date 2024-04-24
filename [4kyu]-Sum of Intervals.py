def sum_of_intervals(intervals: list):
    total_length = 0
    intervals.sort(key=lambda x: x[0])
    current_start, current_end = intervals[0][0], intervals[0][1]
    for start, end in intervals[1:]:
        if start > current_end:
            total_length += current_end - current_start + 1
            current_start, current_end = start, end
        elif start < current_end:
            current_end = end
    total_length =+ current_end - current_start + 1
    return total_length


print(sum_of_intervals([(1, 5), (0, 6)]), 6)
print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
print(sum_of_intervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))
print(sum_of_intervals(( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] )))