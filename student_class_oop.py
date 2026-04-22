class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def greet(self):
        print("Hello", self.name)

s1 = Student("Mahin", 22)
s1.show()
s1.greet()
