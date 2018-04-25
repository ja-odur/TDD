import unittest
from .prime_generator import prime_generator

class prime_tests(unittest.TestCase):

    def test_return_type(self):
        self.assertEqual(type(prime_generator()), list)

    def test_with_start_value_zero(self):
        self.assertEqual(prime_generator(endvalue=20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(prime_generator(endvalue=27), [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_with_start_and_end_values_set(self):
        self.assertEquals()

