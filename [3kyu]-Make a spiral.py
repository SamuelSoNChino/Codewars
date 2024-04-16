def spiralize(size):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    directions = [[1, 1], [0, 1], [1, -1], [0, -1]]
    index = 0
    steps = size
    current = [0, 0]
    while steps > 1:
        direction = directions[index % 4]
        for _ in range(steps - 1):
            if spiral[current[0]][current[1]] == 1:
                direction = directions[(index - 1) % 4]
                current[direction[0]] -= direction[1]
                spiral[current[0]][current[1]] = 0
                current[direction[0]] -= direction[1]
                spiral[current[0]][current[1]] = 0
                steps -= 2
                index -= 1
                break
            else:
                spiral[current[0]][current[1]] = 1
                current[direction[0]] += direction[1]

        index += 1
    if size % 2 == 1:
        spiral[current[0]][current[1]] = 1
    return spiral


for row in spiralize(7):
    print(row)
