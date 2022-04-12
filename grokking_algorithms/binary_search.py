# python -m unittest binary_search.py

from typing import List
from unittest import TestCase

def binary_search(items : List[int], value: int):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if items[mid] == value:
            return mid
        elif items[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return -1


class TestBinarySearch(TestCase):
    def test_even(self):
        items = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(items, 3), 1)

    def test_odd(self):
        items = [1, 3, 5, 7, 9, 13]
        self.assertEqual(binary_search(items, 3), 1)

    def test_not_found(self):
        items = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(items, 60), -1)

    def test_empty_list(self):
        items = []
        self.assertEqual(binary_search(items, 60), -1)
