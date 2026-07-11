class Employee:
    company = "Google"
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

class Programmer:
    company = "Microsoft"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLang(self):
        print(f"The programming language is {self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company)