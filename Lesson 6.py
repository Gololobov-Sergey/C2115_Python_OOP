import random


class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.money = 10000
        self.house = House()
        self.car = car
        self.job = job

    def work(self):
        self.money += 30
        if self.car == None:
            print("Я сходив на роботу")
        else:
            if self.car.drive(20):
                print("Я поїхав на роботу")
            else:
                print("Я сходив на роботу")

    def shopping(self):
        self.money -= random.randint(1,10)
        self.house.food += random.randint(1,10)
        if self.car == None:
            self.money -= 5
            print("Я поїхав в магазин на автобусі")
        else:
            if self.car.drive(random.randint(1,5)*10):
                print("Я поїхав в магазин на авто")
            else:
                self.money -= 5
                print("Я поїхав в магазин на автобусі")

    def chill(self):
        print("Я сьогодні відповиваю")
        self.house.pollution += 2
        self.money -= 5

    def cleaning(self):
        print("Я сьогодні прибираю: ", end='')
        c = random.randint(0,1)
        if c == 0:
            print("повитирали пилюку")
            self.house.pollution -= 2
            if self.house.pollution < 0:
                self.house.pollution = 0
        else:
            print("виконали генеральне прибирання")
            self.house.pollution = 0

    def info(self):
        print(f"Гроші : $ {self.money}")
        if self.car != None:
            self.car.info()
        print(self.house)
        print(self.job)

    def live(self, day):
        self.info()
        if self.money > 500:
            self.car = Car("Lanos")
        self.shopping()

    def is_live(self):
        if self.money < 0:
            return False
        else:
            return True

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60     # l
        self.state = 100   # %

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel < 0:
            print("Подорож не можлива, не вистачає пального")
            return False
        else:
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            print(f"Проїхали {length} км, втратили {delta_fuel} л палива")
            return True


    def addFuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
            print(f"Ми заправили {fuel} л")


    def info(self):
        print(f"Авто {self.model}")
        print(f"Пальне : {self.fuel} л, стан : {self.state} %")


class House:
    def __init__(self):
        self.pollution = 0
        self.food = 0

    def __str__(self):
        return f"Стан будинку:\nЇжа : {self.food}%\nЗабрудненість : {self.pollution}%\n"

class Job:
    def __init__(self, profession, salary):
        self.profession = profession
        self.salary = salary

    def __str__(self):
        return f"Професія : {self.profession}, зарплатня : $ {self.salary}"


human1 = Human("Vasya", job=Job("Programmer", 1000))
for day in range(1, 366):
    if human1.is_live() == False:
        break
    human1.live(day)