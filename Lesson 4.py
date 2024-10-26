import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def study(self):
        print("Я сьогодні навчаюсь")
        self.progress += 5
        self.gladness -= 1

    def sleep(self):
        pass

    def chill(self):
        pass

    def is_alive(self):
        if self.progress < 0:
            print("Мій IQ пішов  вмінус")
            self.alive = False
        elif self.gladness < 0:
            print("В мене дипрессія")
            self.alive = False
        elif self.progress > 500:
            print("Я став розумним")
            self.alive = False

    def info(self):
        print(f"Задоволення - {self.gladness}")
        print(f"Прогрес     - {self.progress}")

    def live(self, day):
        print(f"День {day}")
        print("-"*20)
        choice = random.randint(1, 3)
        if choice == 1:
            self.study()
        elif choice == 2:
            self.sleep()
        elif choice == 3:
            self.chill()

        #


        self.is_alive()
        self.info()
        print()


student = Student("Vasya")
for i in range(1, 366):
    if student.alive == False:
        break
    student.live(i)