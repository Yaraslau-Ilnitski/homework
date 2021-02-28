from random import randint

a = int(input("Введите начало диапазона угадывания\n"))
b = int(input("Введите конец диапазона угадывания\n"))
tries = int(input("Введите количество попыток\n"))
numS = int(randint(a,b))
for i in range(tries):
    numC = int(input("Введите число\n"))
    if numC != numS:
        if i == tries - 1:
            print("You are the looser,the number is: ", numS)
            break
        elif numC > numS:
            print("Искомое число меньше\n")
        else: #  если больше
            print("Искомое число больше\n")
    if numC == numS:
        print("You are the winner")
        break
