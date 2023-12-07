from unittest import TestCase, main

from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("TestGuy", 25000, 100)

    def test_correct_initialization(self):
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)


if __name__ == '__main__':
    main()