from random import randint


def create_matrix(length, height):
    rows = []
    for i in range(length):
        tnp = []
        for s in range(height):
            tnp.append(randint(0, 10))
        rows.append(tnp)
    return rows


matrix = create_matrix(2, 2)


def av(matrix):
    s = 0
    count = 0
    for rowsIndex, rowsValue in enumerate(matrix):
        for tnpIndex, tnpValue in enumerate(rowsValue):
            s += tnpValue
            count += 1
    av = s / count
    return av

average = av(matrix)
print(matrix)
print(average)

def av(matrix):
    s = 0
    count = 0
    for rowsIndex, rowsValue in enumerate(matrix):
        for tnpIndex, tnpValue in enumerate(rowsValue):
            s += tnpValue
            count += 1
    av = s / count
    print(av, s)
