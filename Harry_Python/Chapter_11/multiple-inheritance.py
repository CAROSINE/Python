class Employee:
    company = "Google"
    name = "Mira"
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class Coder:
    language = "Python"
    def printLang(self):
        print(f"The programming language is {self.language}")


class Programmer(Employee, Coder):
    company = "Microsoft"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLang(self):
        print(f"The programming language is {self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company)