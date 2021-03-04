def inch_sant(a):
    n *= 2.54
    print("Inch to sant = ", a)

def centimeter_inch(a):
    a /= 2.54
    print('Centimeters to inch = ', a)
    return a


def mile_kilometre(a):
    a *= 1.609344
    print('Kilometers to mile = ', a)
    return a


def kilometre_mile(a):
    a /= 1.609344
    print('Mile to kilometer = ', a)
    return a


def pounds_kilogram(a):
    a *= 0.4535923745
    print('Kilograms to pounds = ', a)
    return a


def kilogram_pounds(a):
    a /= 0.4535923745
    print('Pounds to kilograms = ', a)
    return a


def ounce_gram(a):
    a *= 28.349523125
    print('Gram in ounce = ', a)
    return a


def gram_ounce(a):
    a /= 28.349523125
    print('Ounce in gram = ', a)
    return a


def gallon_litre(a):
    a *= 3.785411784
    print('Litres in gallon = ', a)
    return a


def litre_gallon(a):
    a /= 3.785411784
    print('Gallons in litres = ', a)
    return a


def pint_litres(a):
    a *= 0.56826125
    print('Litres in pint = ', a)
    return a


def litres_pint(a):
    a /= 0.56826125
    print('Pints in litres = ', a)
    return a
while True:
    n = input('Choose one of the options:\n'
              "inch to sant - 1\n"
              "sant to inch - 2\n"
              "miles to km - 3\n"
              "km to miles - 4\n"
              "pounds to kg - 5\n"
              "kg to pounds - 6\n"
              "ounce to gram - 7\n"
              "gram to ounce - 8\n"
              "galon to litre - 9\n"
              "litres to galon - 10\n"
              "pint to litres - 11\n"
              "litres to pint - 12\n")
    if n.isdigit():
        n = int(n)
        if n == 1:
            a = float(input('Enter the value in centimeters: '))
            inch_centimeter(a)
        elif n == 2:
            a = float(input('Enter the value in inches: '))
            centimeter_inch(a)
        elif n == 3:
            a = float(input('Enter the value in miles: '))
            mile_kilometre(a)
        elif n == 4:
            a = float(input('Enter the value in kilometres: '))
            kilometre_mile(a)
        elif n == 5:
            a = float(input('Enter the value in pounds: '))
            pounds_kilogram(a)
        elif n == 6:
            a = float(input('Enter the value in kilograms: '))
            kilogram_pounds(a)
        elif n == 7:
            a = float(input('Enter the value in ounces: '))
            ounce_gram(a)
        elif n == 8:
            a = float(input('Enter the value in grams: '))
            gram_ounce(a)
        elif n == 9:
            a = float(input('Enter the value in gallons: '))
            gallon_litre(a)
        elif n == 10:
            a = float(input('Enter the value in litres: '))
            litre_gallon(a)
        elif n == 11:
            a = float(input('Enter the value in pints: '))
            pint_litres(a)
        elif n == 12:
            a = float(input('Enter the value in litres: '))
            litres_pint(a)
        elif n == 0:
            break
        else:
            print('Wrong option, try again.')
    else:
        print('Wrong option, try again.')


