class Human:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def addPassenger(self, passenger):
        self.passengers.append(passenger)

    def delPassenger(self, passenger):
        if self.passengers != []:
            self.passengers.remove(passenger)
            return True
        else:
            return False

    def info(self):
        print(f"Auto {self.model}")
        if self.passengers == []:
            print("Зараз в автівці ніхто не їде")
        else:
            print("Зараз в автівці їдуть:")
            for p in self.passengers:
                print(p.name)


human1 = Human("Serg")
human2 = Human("Anna")

car = Car("Tesla Model 13")
car.addPassenger(human1)
car.addPassenger(human2)
car.addPassenger(Human("Vasya"))
# car.info()
car.delPassenger(human1)

car.info()