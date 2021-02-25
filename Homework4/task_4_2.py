a = [1,4,5,7,10]
sum = 0
for i in range(5):
    if a[i] % 2 == 0:
        sum += 1
print("Количество четных чисел = ",sum)

a = [1,4,5,7,10]
sum = 0
i = 0
for i in range(5):
    if a[i] % 2 == 0:
        sum += 1
        i += 1
print("Количество четных чисел = ",sum)

