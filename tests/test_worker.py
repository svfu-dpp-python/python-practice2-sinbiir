import unittest

from worker import Worker


class TestWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.tax_rate = 10
        self.name = 'John Doe'
        self.salary = 100

    def get_worker(self):
        return Worker(self.name, self.salary)

    def test_tax_rate(self):
        self.assertEqual(Worker.tax_rate, self.tax_rate)

    def test_name(self):
        worker = self.get_worker()
        self.assertEqual(worker.name, self.name)

    def test_salary(self):
        worker = self.get_worker()
        self.assertEqual(worker.salary(), self.salary)

    def test_tax(self):
        worker = self.get_worker()
        correct = 10.0
        self.assertAlmostEqual(worker.tax(), correct, 10)
