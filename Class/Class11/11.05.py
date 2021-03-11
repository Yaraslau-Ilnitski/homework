class Dog:

    def __init__(self, weight, name, age):
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump, {self.name}")

    def bark(self):
        print(f"Bark, {self.name}")

    def run(self):
        print(f"Run, {self.name}")

    def rename(self,new_name):
        self.name = new_name


def main():
    dog1 = Dog(20, "Rax", 35)
    print(dog1.name, dog1.weight, dog1.age)
    dog1.jump()
    dog1.run()
    dog1.bark()
    dog1.rename("qwerty")
    dog1.run()

main()
