class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer ("Mahin", 777777, 101028)
print(p.name, p.salary, p.pin, p.company)

r = programmer ("Ahin", 888777, 102028)
print(r.name, r.salary, r.pin, r.company)