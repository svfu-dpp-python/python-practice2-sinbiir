class Worker:
    tax_rate = 10
    
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary
    

    def salary(self):
        return self.sal
    
    def tax_check(self):
        return self.tax_rate

    def tax(self):
        return self.salary() * self.tax_rate / 100
