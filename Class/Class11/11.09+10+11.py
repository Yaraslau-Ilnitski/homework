class Animal:
    name = ''
    age = 0
    master = False
    weight = 0
    height = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print(f"Run {self.name}")

    def jump(self):
        print(f"Jump {self.name}")

    def birthday(self):
        self.age += 1

    def change_weight(self, weight = 0):
        if not weight:
            weight = 0.2
        self.weight += weight

    def change_height(self, height = 0):
        if not height:
            height = 0.2
        self.height += height


class Dog(Animal):

    def bark(self):
        print(f"Bark {self.name}")


class Cat(Animal):

    def meow(self):
        print(f"Meow {self.name}")


class Parrot(Animal):

    def fly(self):
        if self.weight > 0.1:
            print("Parrot can't fly")
            return
        print(f"Fly {self.name}")


def main():
    dog = Dog("Max", 6, False,20,17)
    print(dog.weight,dog.height)
    dog.change_weight()
    dog.change_height()
    print(dog.weight, dog.height)
    parrot = Parrot("Kesha",5,True,0.2,0.2)
    parrot.fly()

if __name__ == '__main__':
    main()
