# Test Driven Development (TDD)
- Write a unit test that fails
- Write production code that passes the test
- Refactor/Clean the code and eliminate redundancies

## Example 
1. Create a new repo called python_TDD
2. Create a new project on pycharm with the same name
3. Create a test file called `calc_test.py` (Naming convention is essential)
4. Create a file called `simple_calc.py` to write code to pass the tests


### Let's import unittest and pytest
- First you need to install both using `pip install pytest`
- Both `unittest` and `pytest` are now installed
```
import unittest
import pytest

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

# Assertions to write out test cases
# We will use our basic calc example to write the tests first then the code

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
```
- On a separate file create a file called simple_calc.py to write code to pass the tests. Naming convention is important.
```
class SimpleCalc:

    def add(self, num1, num2):
        return num1 + num2 # If the outccome is 5 the condition is True the test would pass

    def subtract(self, num1, num2):
        return num1 - num2 # Testing 2 values as boolean

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```
- Run `python -m pytest` on the calc_test.py file to check if all tests have passed.