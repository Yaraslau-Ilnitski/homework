# Открытие файла
#
def main():
    file = open('Texts/Text')  # это наш относительный путь - так как запускаем в этой папке
    print(file)
    file.close()  # не забывать закрывать файл
#
#
# if __name__ == '__main__':
#     main()


# Вывод строчек файла
#
# def main():
#     file = open('Text')
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)
#     file.close()
#
# if __name__ == '__main__':
#     main()

# with open('Text','w') as my_file:
#     my_file.write("Test!")

# import json
# def json_01():
#     with open("json.json", "w") as json_file:
#         data = json.dumps({"name": "ilya", "age": 25})
#         print(data)
#         json_file.write(data)

# def json_02():
#     with open("Texts/json.json") as json_file:
#         data = json.loads(json_file.read())
#         print(data)
#         print(f"Name is {data['first_name']}")
#         if data ['is_teacher']:
#             print("Good")
#
#
# json_02()


