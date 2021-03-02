# def func(**kwargs):
#     for k, value in kwargs.items():
#         print(k, value)
#
#
# print(func(a = 5))

def func(**kwargs):
    for k,value in kwargs.items():
        if len(k) % 2 == 0:
            print(value)
print(func(hellow = 4,qqd="fwef"))
