a = input('Введите слово, имеющее минимум 3 буквы\n')
while True:
    if len(a) < 2:
        print('Слово имеет меньше 3 букв')
        a = input('Введите слово, имеющее минимум 3 буквы\n')
    else:
        b=a[-2]
        print(b)
        break