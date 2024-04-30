def longest_slide_down(pyramid: list[list[int]]):
    def backtrack(modified_pyramid: list[list[int]], index, base_sum, maxes, current_sum) -> list[int] | None:
        if current_sum + maxes[index] < base_sum:
            return None
        if not modified_pyramid:
            return [current_sum]
        sums = []
        for next_step in [index, index + 1]:
            if next_step < len(modified_pyramid[0]):
                possible_sums = backtrack(
                    modified_pyramid[1:], next_step, base_sum, maxes, current_sum + modified_pyramid[0][index])
                if possible_sums:
                    sums += possible_sums
        return sums

    maxes = []
    for i, floor in enumerate(pyramid[::-1]):
        if i:
            maxes.append(maxes[i - 1] + max(floor))
        else:
            maxes.append(max(floor))
    base_sum = 0
    index = 0
    for floor in pyramid:
        if base_sum:
            index = floor.index(max(floor[index:index + 2]))
        base_sum += floor[index]
    return max(backtrack(pyramid, 0, base_sum, maxes[::-1], 0))


print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23)
print(longest_slide_down([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]), 1074)
