summ = 0
while True:
    a = input("Введите число\n")
    if not a.isdigit():
        if a == 'стоп':
            break
        continue
    a = int(a)
    if a % 5 == 0:
        continue
    summ += a
print(summ)