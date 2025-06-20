import unittest
from radix_sort import radix_sort 

class TestRadixSort(unittest.TestCase):
    def test_sort(self):
        test_cases = [
            ([170, 45, 75, 90, 802, 24, 2, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
            ([10, 300, 4, 2000, 50], [4, 10, 50, 300, 2000]),
            ([], []),
            ([5], [5])
        ]
        
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                arr_copy = arr.copy()
                radix_sort(arr_copy)
                self.assertEqual(arr_copy, expected)

if __name__ == '__main__':
    unittest.main()
