import unittest
from quick_sort import quick_sort  

class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        test_cases = [
            ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
            ([5, 3, 8, 6, 2, 7, 1, 4], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([], []),
            ([3], [3])
        ]
        
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                arr_copy = arr.copy()
                quick_sort(arr_copy, 0, len(arr_copy)-1)
                self.assertEqual(arr_copy, expected)

if __name__ == '__main__':
    unittest.main()
