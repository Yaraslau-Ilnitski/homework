from random import randint
import json


def create_matrix(length, height):
    rows = []
    for i in range(length):
        tnp = []
        for i in range(height):
            tnp.append(randint(0, 10))
        rows.append(tnp)
    return rows


def json_01():
    matrix = create_matrix(4, 4)

    with open("Texts/json7.json", "w") as file:
        file.write(json.dumps({"matrix": matrix}))

    with open("Texts/json7.json") as my_file:
        data = json.loads(my_file.read())
        loaded_matrix = data['matrix']

        for parentIndex, rows in enumerate(matrix):
            for valueIndex, value in enumerate(rows):
                if value & 2 == 0:
                    loaded_matrix[parentIndex][valueIndex] = 0
        print(loaded_matrix)

    with open("Texts/json7(2).json", "w") as file:
        file.write(json.dumps({"matrix": loaded_matrix}))


json_01()
