def main():
    with open('Texts/Text5') as incoming:
        even = open("Texts/Text5even", "w")
        odd = open("Texts/Text5.odd", "w")

        for index, line in enumerate(incoming.readlines()):
            diff = (index + 1) % 2
            if diff == 0:
                even.write(line)
            else:
                odd.write(line)
        even.close()
        odd.close()

if __name__ == '__main__':
    main()
