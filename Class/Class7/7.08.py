from math import sqrt


def func(mean_type, *args):
    acc = 0
    count = 0
    if mean_type:
        for item in args:
            acc += item
            count += 1
        return acc / count

    acc = 1
    for item in args:
        acc += item
        count += 1
    return acc ** (1 / count)


func(False, 1, 2, 3)
