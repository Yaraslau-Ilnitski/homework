def main():
    lines = []
    file = open('Texts/Text')
    while True:
        line = file.readline()
        lines.append(line)
        if not line:
            break
    print(lines[0])  # недоделали
    print(lines[2])
    print(lines[::-1])
    file.close()



if __name__ == '__main__':
    main()

