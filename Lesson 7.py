
class Human:
    def __init__(self, name, height, rabota="?????"):
        self.__name = name
        self.__height = 170
        self.setHeight(height)
        self.__rabota = rabota

    def setHeight(self, height):
        if height < 200:
            self.__height = height

    def getHeight(self):
        return self.__height

    def info(self):
        print(f"Name   - {self.__name}")
        print(f"Zrist  - {self.__height}")
        print(f"Rabota - {self.__rabota}")



class Student(Human):

    def __init__(self, name, height, rabota, iq=100):
        self.iq = iq
        super().__init__(name, height, rabota)

    def study(self):
       print("I`m study")

    def info(self):
        super().info()
        print(f"IQ     - {self.iq}")



h = Human("Vasya", 160)
h.setHeight(170)
print(h.getHeight())
h.info()



s = Student("Kolya", 190, "IT STEP", 120)
s.info()

