import unittest
from the_greedy_algorithm_7 import max_flowers

class TestFlowerField(unittest.TestCase):
    def test_small_grid(self):
        grid = [
            "101",
            "110"
        ]
        self.assertEqual(max_flowers(grid, 2, 3), 3)

    def test_3x3_grid(self):
        grid = [
            "100",
            "110",
            "001"
        ]
        self.assertEqual(max_flowers(grid, 3, 3), 2)

    def test_single_cell(self):
        grid = ["1"]
        self.assertEqual(max_flowers(grid, 1, 1), 1)

    def test_no_flowers(self):
        grid = [
            "000",
            "000"
        ]
        self.assertEqual(max_flowers(grid, 2, 3), 0)

    def test_large_grid(self):
        grid = [
            "111",
            "111",
            "111"
        ]
        self.assertEqual(max_flowers(grid, 3, 3), 5)

if __name__ == "__main__":
    unittest.main()
