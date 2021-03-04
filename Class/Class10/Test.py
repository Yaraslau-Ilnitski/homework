# Открытие файла

def main():
    file = open('Text')  # это наш относительный путь - так как запускаем в этой папке
    print(file)
    file.close()  # не забывать закрывать файл


if __name__ == '__main__':
    main()
