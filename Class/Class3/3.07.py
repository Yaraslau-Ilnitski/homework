stroka = input("Введите предложение\n")
if len(stroka) > 5 :
    print(stroka)
elif len(stroka) < 5:
    print("Need more!")
elif len(stroka) == 5:
    print("It is five")