from random import randint

class Train:
    def book(self, trainNo, frm, to):
        print(f"Ticket is booked in train no {trainNo} from {frm} to {to}")

    def getStatus(self, trainNo):
        print(f"Ticket is running successfully in train no {trainNo} and status is on time")

    def getFare(self, trainNo, frm , to):
        print(f"Ticket is fair in train no {trainNo} from {frm} to {to} is {randint(408, 302)}")

# instantiate Train and call methods
a = Train()
a.getStatus(1028)
a.book(1028, "Delhi", "Mumbai")  # we can use here a. or something else 