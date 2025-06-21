import unittest
from merge_sort import merge_sort
from radix_sort import radix_sort
from quick_sort import quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_radix_sort(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2]), [2, 24, 45, 75, 90, 170, 802])
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([1]), [1])
        self.assertEqual(radix_sort([100, 10, 1]), [1, 10, 100])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
