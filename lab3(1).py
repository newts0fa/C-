import unittest
from merge_sort import merge_sort  

class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        test_cases = [
            ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([], []),
            ([1], [1])
        ]
        
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                arr_copy = arr.copy()
                merge_sort(arr_copy)
                self.assertEqual(arr_copy, expected)

if __name__ == '__main__':
    unittest.main()
