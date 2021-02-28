a = [1,4,5,7,10]
a_new = []
n = 0
while n < len(a):
    a_new.insert(0, a[-n])
    n += 1
print(a_new)


a = [1,4,5,7,10]
a_new = []
n = 0
for i in range(len(a)):
    a_new.insert(0, a[-n])
    n += 1
print(a_new)
