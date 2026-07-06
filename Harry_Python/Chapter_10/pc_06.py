from random import randint

class Train:
    def __init__(slf, trainNo, frm, to):
        slf.trainNo = trainNo
        slf.frm = frm
        slf.to = to

    def book(slf, trainNo, frm, to):
        print(f"Ticket is booked in train no {slf.trainNo} from {slf.frm} to {slf.to}")

    def getStatus(slf, trainNo):
        print(f"Ticket is running successfully in train no {slf.trainNo} and status is on time")

    def getFare(slf, trainNo, frm , to):
        print(f"Ticket is fair in train no {slf.trainNo} from {slf.frm} to {slf.to} is {randint(408, 302)}")

# instantiate Train and call methods
a = Train(1028, "Delhi", "Mumbai")
a.getStatus(1028)
a.book(1028, "Delhi", "Mumbai")  # we can use here a. or something else 