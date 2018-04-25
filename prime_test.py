import unittest
from .prime_generator import prime_generator


class prime_tests(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(prime_generator()), list, msg='The returned type does not match the type list' )

    def test_default(self):
        self.assertEqual(prime_generator(), [2])

    def test_with_start_value_zero(self):
        self.assertEqual(prime_generator(end_value=20), [2, 3, 5, 7, 11, 13, 17, 19], msg='The expected output differs')
        self.assertEqual(prime_generator(end_value=27), [2, 3, 5, 7, 11, 13, 17, 19, 23], msg='The expected output differs')

    def test_with_start_and_end_values_set(self):
        self.assertEqual(prime_generator(start_value=3, end_value=18), [3, 5, 7, 11, 13, 17], msg='The expected output differs')


if __name__ == '__main__':
    unittest.main()