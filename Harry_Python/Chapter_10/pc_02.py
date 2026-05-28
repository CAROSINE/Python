class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")
 
                 # or  
a = Calculator   # a = Calculator(5)
a(5).square()    # a.square()