list = [1,4,5,7,10]
l = len(list)
sum = 0
for i in range(l):
    if list[i] % 2 == 0:
        sum += 1
print("Количество четных чисел = ",sum)

list = [1,4,5,7,10]
sum = 0
l = len(list)
i = 0
while i < l:
    if list[i] % 2 == 0:
        sum += 1
    i += 1
print("Количество четных чисел = ",sum)

