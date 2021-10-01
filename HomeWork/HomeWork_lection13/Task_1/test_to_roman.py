import unittest
from to_roman import to_roman, NonValidInput


class ToRomanTestMethods(unittest.TestCase):

    def test_type_of_data(self):
        self.assertRaises(Exception, to_roman, 'asd')

    def test_answer(self):
        self.assertEqual('V', to_roman(5))

    def test_out_of_range(self):
        self.assertEqual(1, to_roman(6000))


if __name__ == '__main__':
    unittest.main()



