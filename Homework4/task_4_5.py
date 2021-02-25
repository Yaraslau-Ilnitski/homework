fib_list = []
fib = 1
n = 0
fib_list.append(fib)

while n < 14:
    fib_list.append(fib)
    fib += fib_list[n]
    n += 1
print(fib_list)


fib_list = []
fib = 1
n = 0
fib_list.append(fib)

for i in range(14):
    fib_list.append(fib)
    fib += fib_list[n]
    n += 1
print(fib_list)
