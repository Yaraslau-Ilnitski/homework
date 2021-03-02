from random import randint


def create_matrix(length, height):
    rows = []
    for i in range(length):
        tnp = []
        for i in range(height):
            tnp.append(randint(0, 10))
        rows.append(tnp)
    return rows


matrix = create_matrix(2, 2)


def view(matrix):
    for vert in matrix:
        for item in vert:
            print(item)


# print(matrix)
# view(matrix)


def sum(matrix):
    s = 0
    for valueList in matrix:
        for i in valueList:
            s += i
    return s


# print(matrix)
# print(sum(matrix))


def greatest(matrix):
    greatest = 0
    for valueRows in matrix:
        for valueTNP in valueRows:
            if valueTNP > greatest:
                greatest = valueTNP
    return greatest


# print(greatest(matrix))


def minimum(matrix):
    minimum = matrix[0][0]  # берем значение как первый элемент матрицы
    for valueRows in matrix:
        for valueTNP in valueRows:
            if minimum > valueTNP:
                minimum = valueTNP
    return minimum


print(matrix)
print(minimum(matrix))
