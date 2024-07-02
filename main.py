from worker import Worker
from bonus_worker import BonusWorker

def format_worker(worker):
    name = worker.name.ljust(30)
    salary = f"{worker.salary():10.2f}"
    tax = f"{worker.tax():10.2f}"
    net_salary = f"{worker.salary() - worker.tax():10.2f}"
    return f"{name}{salary}{tax}{net_salary}"
