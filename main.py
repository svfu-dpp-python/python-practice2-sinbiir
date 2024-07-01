from worker import Worker
from bonus_worker import BonusWorker

def format_worker(worker):
    name = worker.name.ljust(30)
    salary = f"{worker.salary} "
    tax = f"{worker.tax()} "
    net_salary = f"{worker.salary - worker.tax()}"
    return f"{name}{salary}{tax}{net_salary}"

if __name__ == "__main__":
    bob = BonusWorker("Негр", 1000, 10)
    print(format_worker(bob))
