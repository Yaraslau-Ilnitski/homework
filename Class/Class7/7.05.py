def func(*args):
    s = 0
    for index,element in enumerate(args):
        s += element * index
    return s


print(func(1, 2, 3))