class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display(self):
        print("ID:", self.id)

s = Student("Mahin", 101)
s.show()
s.display()
