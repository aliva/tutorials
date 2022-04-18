# python -m unittest quick_sort_with_partations.py

from typing import List
from unittest import TestCase


def partation(items: List[int], low: int, high: int) -> int:
    pivot = items[high]

    i = low

    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i += 1

    items[i], items[high] = items[high], items[i]
    return i


def quick_sort(items: List[int], low: int, high: int):
    if low < high:
        pivot = partation(items, low, high)

        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)


class TestQuickSort(TestCase):
    def test_sort(self):
        items = [5, 3, 6, 2, 10]
        sorted_items = [2, 3, 5, 6, 10]

        quick_sort(items, 0, len(items) - 1)
        self.assertEqual(items, sorted_items)

    def test_empty(self):
        items = []
        sorted_items = []


        quick_sort(items, 0, len(items) - 1)
        self.assertEqual(items, sorted_items)
