a = int(input("Введите число делящееся на 1000:\n"))
while True:
    if a % 1000 == 0:
        print('millenium')
        break
    else:
        a = int(input("...\nВведите число делящееся на 1000:\n"))
