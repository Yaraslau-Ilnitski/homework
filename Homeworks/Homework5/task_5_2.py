a = input("Введите число")
def count_numbers(value):
    s = 0
    m = 1
    for i in range(len(a)):
        s += int(a[i])
        m *= int(a[i])
    print("Сумма =",s,"Произведение =",m)
count_numbers(a)