import unittest
import logging
class Runner:
    def __init__(self, name: str, speed: int = 1):
        if not isinstance(name, str):
            raise TypeError("Имя бегуна должно быть строкой")
        if speed < 0:
            raise ValueError("Скорость бегуна не может быть отрицательной")
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10

class RunnerTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='runner_tests.log',
            filemode='w',
            encoding='utf-8'
        )

    def test_walk(self):
        try:
            runner = Runner("Коля", -1)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Скорость не может быть отрицательной")
            runner = Runner("Коля")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Расстояние после 10 прогулок должно быть 50")


    def test_run(self):
        try:
            runner = Runner(123)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            runner = Runner("Наташа")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Расстояние после 10 забегов должно быть 100")

    def test_challenge(self):
        runner1 = Runner("Коля")
        runner2 = Runner("Наташа")

        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Дистанции для бегунов должны быть разными")

    if __name__ == '__main__':
        unittest.main()
