from random import randint
def create_matrix(length):
    rows = []
    for i in range(length):
        tnp = []
        for s in range(length):
            tnp.append(randint(0,10))
        rows.append(tnp)
    return rows
print(create_matrix(2))
