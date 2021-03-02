from random import randint

a = input("Введите начало диапазона угадывания\n")
while True:  # проверка на int значение
    try:
        a = int(a)
        break
    except ValueError:
        print("Вы ввели не число,попробуйте еще раз\n")
        a = input("Введите начало диапазона угадывания\n")

b = input("Введите конец диапазона угадывания\n")
while True:  # проверка на int значение
    try:
        b = int(b)
        break
    except ValueError:
        print("Вы ввели не число,попробуйте еще раз\n")
        b = input("Введите конец диапазона угадывания\n")
tries = input("Введите количество попыток\n")
while True:  # проверка на int значение
    try:
        tries = int(tries)
        break
    except ValueError:
        print("Вы ввели не число,попробуйте еще раз\n")
        tries = input("Введите количество попыток\n")

numS = int(randint(a, b))

for i in range(tries):
    numC = input("Попробуйте угадать число\n")
    while True:
        try:
            numC = int(numC)
            break
        except ValueError:
            print("Вы ввели не число\n")
            numC = input("Введите число\n")
    if numC != numS:
        if i == tries - 1:
            print("You are the looser,the number is: ", numS)
            break
        elif numC > numS:
            print("Искомое число меньше\n")
        else:  # если больше
            print("Искомое число больше\n")
    if numC == numS:
        print("You are the winner")
        print("Колмчество попыток:", i + 1)
        break
