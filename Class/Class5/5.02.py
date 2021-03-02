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

def sum_of_elements_by_divider(matrix, divider):
    s = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem % divider == 0:
                s += matrixItem
    return s
print(matrix)
print(sum_of_elements_by_divider(matrix,3))