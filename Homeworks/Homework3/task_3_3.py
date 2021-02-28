a = input("Введите строку:\n")
if len(a) > 10:
    b = input("Введите строку:\n")
    b += "!!!"
    print(b)
elif len(a) < 10:
    print(a[1])
else:
    print(10 / 10)
