class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print("Sum:", self.x + self.y)

    def sub(self):
        print("Sub:", self.x - self.y)

    def mul(self):
        print("Mul:", self.x * self.y)

c = Calculator(10, 5)
c.add()
c.sub()
c.mul()
