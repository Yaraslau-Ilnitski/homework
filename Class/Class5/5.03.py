from random import randint
def create_matrix(length):
    rows = []
    for i in range(length):
        tnp = []
        for s in range(length):
            tnp.append(randint(0,10))
        rows.append(tnp)
    return rows

matrix = create_matrix(2)

def founded_elem(matrix,found):
    s = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem == found:
                s += 1
    return s
print(matrix)
print(founded_elem(matrix,7))