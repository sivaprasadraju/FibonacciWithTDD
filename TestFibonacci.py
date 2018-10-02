import unittest
import pytest
from main import *

class FibonacciTests(unittest.TestCase):

    def test_fibonacci(self):
        correct_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        response = fibonacci(13)
        self.assertEquals(len(response), len(correct_sequence))

    def test_fibonacciSeries(self):
        correct_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        response = fibonacci(13)
        for index in range(len(response)):
            self.assertEquals(response[index], correct_sequence[index])

    def test_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-1)
