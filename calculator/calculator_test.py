__author__ = 'Fran'

import unittest
from calculator import add , subtract

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        result = add(2,2)
        self.assertEqual(result , 4)

    def test_subtract(self):
        result = subtract(5,3)
        self.assertEqual(result,2)


if __name__ == '__main__':
    unittest.main()
