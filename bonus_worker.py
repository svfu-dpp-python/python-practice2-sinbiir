from worker import Worker

class BonusWorker(Worker):
    
    def __init__(self, name, salary, bonus_percent):
        super().__init__(name, salary)
        self.bonus_percent = bonus_percent

    def salary(self):
        return super().salary() * (1 + self.bonus_percent / 100)
