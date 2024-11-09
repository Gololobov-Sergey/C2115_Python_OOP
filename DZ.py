import random


class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.mani = 100
        self.house = House()
        self.car = car
        self.job = job
        self.counter = 0
        self.alive = True

    def work(self):
        self.mani += 100
        if self.car == None:
            print("Я ПОШЁЛ на работу")
            self.counter += 1
        else:
            if self.car.drive(20):
                print("Я ПОЕХАЛ на работу")
            else:
                print("Мне не хватило топлива на поездку")

    def shoping(self):
        self.mani -= random.randint(1,100)
        self.house.food += random.randint(1,25)
        if self.car == None:
            print("Я ПОЕХАЛ в магазин на автобусе")
            self.mani -= 25
        else:
            if self.car.drive(random.randint(1,5)*10):
                print("Я ПОЕХАЛ в магазин на машине")
            else:
                print("Мне не хватило топлива на поездку, и я поехал на автобусе")
                self.mani -= 25

    def check(self):
        if self.mani < 0:
            print("Я бомж")
            self.alive = False
        if self.house.pollution >= 100:
            print("Я засрал дом и он взорвался")
            self.alive = False
        if self.house.food <= 0:
            print("Я голодный и я помэр")
            self.alive = False
        if self.house.sloman >= 100:
            print("Мой дом сломался")
            self.alive = False
    def chill(self):
        print("Я сегодня отдыхаю")
        self.house.pollution += 5
        self.mani -= 10

    def repair(self):
         if self.car and self.car.state < 10:
             print("Вы отправили машину на СТО")
             self.mani -= 10
             self.car.state += 90



    def info(self):
        print(f"Деньги: {self.mani} $")
        if self.car != None:
            self.car.info()
        print(self.house)
        print(self.job)


    def live(self, day):
        print(f"День: {day} ")
        self.info()
        if self.mani > 1 and self.car == None :
            self.car = Car("lkjlkjl")
            print("У вас появилась машина.")
            self.mani -= 1
        sigma = random.randint(1,5)
        if sigma == 1:
            self.work()
        if sigma == 2:
            self.shoping()
        if sigma == 3:
            self.chill()
        if sigma == 4:
            self.repair()
        if sigma == 5:
            print("Я заправил машину")
            if self.car != None:
                if self.car.fuel + self.car.fuel <= 60:
                    self.car.fuel += self.car.fuel
                    print("Вы заправились на", self.car.fuel, "литров")
        self.house.food -= 10
        self.check()



        if self.mani < 0:
            return False
        else:
            return True




    def cleaning(self):
        if self.house.pollution > 80:
            print("Я сегодня вызываю клиниг")
            self.house.pollution -= random.randint(50, 80)
            self.mani -= 10
        else:
            print("Я убираюсь сам")
            self.house.pollution -= random.randint(1, 30)
        if self.house.pollution < 0:
            self.house.pollution = 0

    def cleaning1(self):
        print("Я сегодня убираю:", end='')
        c = random.randint(0,1)




class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60 # L
        self.state = 100 # %

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel < 0:
            print("Поездка не возможна, не хватает топлива")
            return False
        else:
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            print(f"Проехали{length}км, {delta_fuel} литров топлива использовали")
            return True

    def addFuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
            print("Вы заправились на", fuel, "литров")

    def info(self):
        print(f"Auto: {self.model}")
        print(f"Топливо: {self.fuel} л, стан: {self.state}%")


class House:
    def __init__(self):
        self.pollution = 0
        self.sloman = 0
        self.food = 100

    def __str__(self):
        return f"Дом:\nЕда: {self.food}%\nЗамусоренность: {self.pollution}%\n"

class Job:
    def __init__(self, profession, salary):
        self.profesia = profession
        self.salary = salary

    def __str__(self):
        return f"Професия: {self.profesia}, зарплата: $ {self.salary}"






human1 = Human("Vasya", job = Job("Programmer", 1000))
for day in range(1, 365):
    if human1.alive == False:
        break
    else:
        human1.live(day)

