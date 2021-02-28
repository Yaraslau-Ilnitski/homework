age = int(input("Введите возраст\n"))
if age < 0:
    print("Wrong input")
elif age < 18:
    print("CocaCola")
else:
    print("Beer")