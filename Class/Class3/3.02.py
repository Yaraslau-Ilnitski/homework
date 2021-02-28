a = int(input("Введите число\n"))
b = int(input("Введите число\n"))
print(f"{a} + {b} = ",a + b)

a = int(input("Введите число\n"))
b = int(input("Введите число\n"))
print("{} + {} = ".format (a, b),a+b)

a = int(input("Введите число\n"))
b = int(input("Введите число\n"))
print("{1} + {0} = ".format (b, a),a+b)

a = int(input("Введите число\n"))
b = int(input("Введите число\n"))
print("%s + %s = " % (a, b),a+b)
