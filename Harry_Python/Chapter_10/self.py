class Employee:
    language = "Python" # class attribute
    salary = 300000

    def getInfo(self):    # it's a method
         print(f"The language is {self.language}. The salary is {self.salary}")

Ahin  = Employee()
Ahin.language= "JavaScript" # it's an instance attribute

Ahin.getInfo() # after this line , this line appears "Employee.getInfo()"
               # so we wrote getInfo(self)


# Create method