import unittest
from Search_with_refund import solve_n_queens

class TestNQueens(unittest.TestCase):
    def test_n_1(self):
        expected = [["Q"]]
        self.assertEqual(solve_n_queens(1), expected)

    def test_n_2(self):
        self.assertEqual(solve_n_queens(2), [])

    def test_n_4(self):
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)
        expected_solution = [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ]
        self.assertIn(expected_solution, solutions)

    def test_n_8(self):
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92)

if __name__ == "__main__":
    unittest.main()
