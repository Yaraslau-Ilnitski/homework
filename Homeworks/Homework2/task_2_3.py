a = input('Введите слово, имеющее минимум 5 букв:\n')
while True:
    if len(a) < 5:
        print('Слово имеет меньше 5 букв.')
        a = input('Введите слово, имеющее минимум 5 букв:\n')
    else:
        b = a[0:5]
        print(b)
        break
