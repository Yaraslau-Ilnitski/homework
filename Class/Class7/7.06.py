# def func(a,b):
#     sum = a + b
#     dif = a - b
#     print(sum,dif)
# sum,dif = func(2,3)

def func(*args):
    s = 0
    greatest = args[0]
    for i in args:
        s += i
        if i > greatest:
            greatest = i
    return s,greatest
print(func(1,2,3))
