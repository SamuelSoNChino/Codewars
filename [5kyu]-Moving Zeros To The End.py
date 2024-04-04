def move_zeros(lst):
    zeros = []
    new = []
    for element in lst:
        if element != 0:
            new.append(element)
        else:
            zeros.append(0)
    return new + zeros
