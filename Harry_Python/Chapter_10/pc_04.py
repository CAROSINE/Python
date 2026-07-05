class Calculator:

    def __init__(self, n):
        self.n = n
  
    def square(self):
        print(f"The square is {self.n * self.n}")


    @staticmethod
    def hello():
        print("Hello World__ :)")
      
                 # or  
a = Calculator   # a = Calculator(5)
a(5).square()    # a.square()
a.hello()       # a.hello()