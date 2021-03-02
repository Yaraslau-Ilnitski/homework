from random import randint


def factorial(number):  # факториал
    s = 1
    for i in range(number + 1):
        if i < 1:
            continue
        s *= i
    print(s)


factorial(randint(0,10)

def fact_recursive(n):  # рекурсивный факториал
    if n <= 1:
        return 1
    return n * fact_recursive(n - 1)


# print(fact_recursive(1))

def fib(n):  # рекурсивная сумма чисел фибоначи
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(6))
