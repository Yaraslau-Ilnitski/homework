a = [21, 12, 11, 1, 12, -2]
s = 0
for i in range(len(a)):
    if a[i] > 10:
        s += a[i]
    i += 1
print(s)
