def main():
    with open('Texts/Text4') as incoming:
        with open("Texts/Text4.2", "w") as output:
            for line in incoming.readlines():
                print(f"before {line}")
                edited = line.replace("0", "@").replace("1", "0").replace("@", "1")
                print(f"after {line}")

                output.write(edited)


if __name__ == '__main__':
    main()
