import unittest

from Task_2 import Primes, check_prime


class PrimesIteratorTest(unittest.TestCase):

    def test_Primes(self):
        self.assertEqual(list(Primes(5)), [2, 3])

    def test_type_of_data(self):
        self.assertRaises(Exception, Primes(-1), 'asd')


if __name__ == '__main__':
    unittest.main()
