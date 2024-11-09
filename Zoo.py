
class Animal:
    def __init__(self, name):
        self.__name = name

    def info(self):
        print("Name:", self.__name)

class Mammals(Animal):
    def run(self):
        print("I`m run")


class Bird(Animal):
    pass


class Cat(Mammals):
    def __init__(self, name, mouse):
        super().__init__(name)
        self.__mouse = mouse

    def info(self):
        super().info()
        print("Mouse:", self.__mouse)

    def cathMouse(self):
        print("I`m catc a mouse")
        self.__mouse += 1

class Dog(Mammals):
    pass

class Cow(Mammals):
    pass

class Sparrow(Bird):
    pass

class Eagle(Bird):
    pass


cat = Cat("Tom", 10)
cat.run()
cat.cathMouse()
cat.info()

# sp = Sparrow()
