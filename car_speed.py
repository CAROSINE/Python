# Car speed control using class

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
        

    def accelerate(self):
        self.speed += 10
        print("Speed increased to:", self.speed)
        

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        print("Speed decreased to:", self.speed)
        

    def show(self):
        print("Car:", self.brand, "| Speed:", self.speed)


# object create
c1 = Car("Toyota")
c1.accelerate()
c1.accelerate()
c1.brake()
c1.show()
