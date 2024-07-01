class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tax_rate = 10

    def salary(self):
        return self.salary
    
    def tax_rate(self):
        return self.tax_rate

    def tax(self):
        return self.salary * self.tax_rate / 100
