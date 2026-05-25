class Employee:
    language = "Python" # class attribute
    salary = 300000

    def __init__(self, name, salary, language):     # dunder method , automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creting an object")


    def getInfo(self):    # it's a method
         print(f"The language is {self.language}. The salary is {self.salary}")
 
    
    @staticmethod
    def greet():   # another method
        print("Good Morning✨")

Ahin  = Employee("Ahin", 500000, "Bitrox")   # creating an object of class Employee
# Ahin.name= "Mahin"
print(Ahin.name, Ahin.salary)

# rohan = Employee("Rohan", 400000, "JavaScript")  # bcz of dunder method , line 5 will called 