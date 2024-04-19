def smaller(arr):
    num = []
    new = []
    for i in arr:
        for j in range(len(num)):
            if i < num[j]:
                new[j] += 1
        num.append(i)
        new.append(0)
    return new



print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), [0, 0, 0])