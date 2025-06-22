import unittest
from Divide_and_conquer_2 import find_first_occurrence, find_last_occurrence, find_occurrences

class TestBinarySearch(unittest.TestCase):
    def test_find_first_occurrence(self):
        nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
        self.assertEqual(find_first_occurrence(nums, 5), 1)
        self.assertEqual(find_first_occurrence(nums, 6), 4)
        self.assertEqual(find_first_occurrence(nums, 9), 7)
        self.assertEqual(find_first_occurrence(nums, 4), -1)

    def test_find_last_occurrence(self):
        nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
        self.assertEqual(find_last_occurrence(nums, 5), 3)
        self.assertEqual(find_last_occurrence(nums, 6), 5)
        self.assertEqual(find_last_occurrence(nums, 9), 9)
        self.assertEqual(find_last_occurrence(nums, 4), -1)

    def test_find_occurrences(self):
        nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
        self.assertEqual(
            find_occurrences(nums, 5),
            "The first occurrence of element 5 is located at index 1\n"
            "The last occurrence of element 5 is located at index 3",
        )
        self.assertEqual(
            find_occurrences(nums, 4),
            "Element not found in the array",
        )

if __name__ == "__main__":
    unittest.main()
