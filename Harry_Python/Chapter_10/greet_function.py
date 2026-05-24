class Employee:
    language = "Python" # class attribute
    salary = 300000

    def getInfo(self):    # it's a method
         print(f"The language is {self.language}. The salary is {self.salary}")
 

    def greet(self):   # another method
        print("Good Morning✨")

Ahin  = Employee()
Ahin.greet() 
Ahin.getInfo()
# self ia parameter