# Simple Calculator using OOP

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b 

    def subtract(self):
        return self.a - self.b

# object create
calc = Calculator(10, 5)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())