from datetime import datetime
time = datetime.now()

def decorator(func):
    def wrap():
        start_at = time.time()
        func()
        end_at = time.time()
        print(end_at - start_at)
    return wrap

@decorator
def factorial(number = 19999):  # факториал
    s = 1
    for i in range(number + 1):
        if i < 1:
            continue
        s *= i


factorial()

