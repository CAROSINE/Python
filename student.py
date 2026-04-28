# Student Information System using OOP

class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.dept)

# object create
s1 = Student("Mahin", 22, "CSE")

s1.display()