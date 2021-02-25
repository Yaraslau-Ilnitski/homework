# for i,elem in enumerate(['a','b','c','d']):
#     print(f"{i} - {elem}")
#
#
# from random import randint
#
# def create_matrix(length, height):
#     rows = []
#     for _ in range(length):
#         tnp = []
#         for _ in range(height):
#             tnp.append(randint(0, 10))
#         rows.append(tnp)
#
#     return rows
#
#
#
# matrix = create_matrix(2,3)
# print(matrix)
#
# def calc_av_sum(matrix):
#     count = 0
#     sum = 0
#     for parentList in matrix:
#         for matrixItem in parentList:
#             count += 1
#             sum += matrixItem
#     return sum / count
#
# average = calc_av_sum(matrix)
# print(average)
#
# def calc_elements(matrix, average):
#     count = 0
#     for parentInd, parentList in enumerate(matrix):
#         for childInd, child in enumerate(parentList):
#             if child < average:
#                 continue
#             if (parentInd + childInd) % 2 != 0:
#                 continue
#             print(f"found! p-in {parentInd},ch-in {childInd},value {child}")
#             count += 1
#     return count
# print(calc_elements(matrix, average))
#
#
#
# 5.06
# pupils = [
#     {
#         "firstname":"Masha",
#         "group":41,
#         "physics":7,
#         "math":9,
#     },
#     {
#         "firstname":"kolya",
#         "group":24,
#         "physics":9,
#         "math":1,
#     },
#     {
#         "firstname": "Olya",
#         "group": 12,
#         "physics": 8,
#         "math": 6,
#     }
# ]
# def meh(users):
#     sum = 0
#     for user in users:
#         av = (user["physics"] +user["math"] / 2
#         user["average"] = av



