import unittest
from Tree_4 import func

class TestBSTCount(unittest.TestCase):
    def test_n0(self):
        self.assertEqual(func(0), 1)  # Пустое дерево

    def test_n1(self):
        self.assertEqual(func(1), 1)  # Только корень

    def test_n2(self):
        self.assertEqual(func(2), 2)  # Два возможных дерева

    def test_n3(self):
        self.assertEqual(func(3), 5)  # Пример из условия

    def test_n4(self):
        self.assertEqual(func(4), 14)  # Пример из условия

    def test_n5(self):
        self.assertEqual(func(5), 42)  # C₅ = 42

    def test_invalid_n(self):
        self.assertEqual(func(-1), 0)  # Некорректный ввод
        self.assertEqual(func(21), 0)  # Превышение ограничения

if __name__ == "__main__":
    unittest.main()
