from random import randint # че-то другое в итоге сделали))


def create_matrix(length = 3, height=2):
    rows = []
    for i in range(length):
        tnp = []
        for i in range(height):
            tnp.append(randint(0, 10))
        rows.append(tnp)
    return rows
print(create_matrix())
