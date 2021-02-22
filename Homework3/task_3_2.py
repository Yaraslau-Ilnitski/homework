a = int(input("Введите количество гостей:\n"))
if a > 50:
    print('Заказать ресторан')
elif 20 <= a <= 50:
    print('Заказать кафе')
elif 0 < a < 20:
    print("Заказать дом")
elif a <= 0:
    print("Such a lonely day, and its mine..")
