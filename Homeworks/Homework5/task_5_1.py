def summ(a, b):
    return (a + b)


def diff(a, b):
    return (a - b)


def mult(a, b):
    return (a * b)


def div(a, b):
    return (a / b)


while True:

    a = int(input('Введите число a :\n'))
    b = int(input('Введите число b :\n'))

    while True:
        c = input("Введите знак '+','-','/','*' или '0' для ввода новых чисел или выхода из калькулятора :\n")
        if c == '+':
            print(a, '+', b, '=', summ(a, b))
        if c == '-':
            print(a, '-', b, '=', diff(a, b))
        if c == '*':
            print(a, '*', b, '=', mult(a, b))
        if c == '/':
            if b == 0:
                print("На ноль делить низя\n")
                continue
            print(a, '/', b, '=', div(a, b))
        if c == '0':
            break

    d = input("Хотите продолжить:Да/Нет\n")
    if d == "Да":
        continue
    elif d == "Нет":
        break
    else:
        print("Допустим это было 'Да'\n")
