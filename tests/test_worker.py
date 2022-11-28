from unittest import TestCase

from worker import Worker


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.tax_rate = 10
        self.name = 'John Doe'
        self.salary = 100
        self.worker = Worker(self.name, self.salary)

    def test_tax_rate(self):
        self.assertEqual(Worker.tax_rate, self.tax_rate)

    def test_name(self):
        self.assertEqual(self.worker.name, self.name)

    def test_salary(self):
        self.assertEqual(self.worker.salary(), self.salary)

    def test_tax(self):
        self.assertEqual(self.worker.tax(), self.salary * self.tax_rate)
