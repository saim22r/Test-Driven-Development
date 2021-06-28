# Let's import unittest and pytest

import unittest
import pytest

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

# assertions to write out test cases
# we will use our basic calc example to write the tests first then the code

    def test_add(self):
        # Naming convention is essential to have the test in the name of our method
        self.assertEqual(self.calc.add(3, 2), 5) # if True test would pass
        # return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4) # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)  # 6 / 3