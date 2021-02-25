a = [1,4,5,7,10]
while True:
    a =[a[-1]] + a[:-1]
    break
print(a)

a = [1,4,5,7,10]
for i in range(1):
    a[0:1] = [a.pop(),a[0]]
print(a)
