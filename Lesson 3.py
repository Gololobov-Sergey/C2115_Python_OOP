
class Student:

    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        if age < 100:
            self.age = age
        else:
            self.age = 15
        self.iq = 100
        #print(f"{name} народився")

    def study(self):
        if self.iq < 180:
            self.iq += 5
        print("Я навчаюсь")

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"IQ   : {self.iq}")

    def __str__(self):
        return f"Name : {self.name}\n" + f"Age  : {self.age}\n" + f"IQ   : {self.iq}\n" + f"Height : {self.iq}\n"


st1 = Student("Vasya", 20, 150)
st2 = Student("Kolya", 21, 170)
print(st1)

st1.height = 100500

st1.study()
st1.study()
st1.study()
st1.study()
st1.study()
st1.study()

st1.info()



# st2 = Student("Ira", 17)
# print(st2.name)
# print(st2.age)
#
# if st1.age < st2.age:
#     print(f"{st2.name} старший")
# else:
#     print(f"{st1.name} старший")