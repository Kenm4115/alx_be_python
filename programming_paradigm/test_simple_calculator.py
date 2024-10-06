
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of SimpleCalculator for use in tests."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()


"""
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

Provided: simple_calculator.py
You’re given a SimpleCalculator class with basic arithmetic operations. Your task is to write unit tests to verify its correctness.
Task: Write Unit Tests in test_simple_calculator.py
Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.

Guidelines for Writing Tests:
Import the Necessary Modules:

Import the unittest module and the SimpleCalculator class from simple_calculator.py.
Define a Test Class:

Create a test class that inherits from unittest.TestCase.
Write Test Methods:

Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
Include tests for edge cases, such as dividing by zero.
Use Assertions to Verify Results:

Utilize self.assertEqual() to check for expected outcomes.
For the divide method, ensure you test both normal operation and division by zero.
Running Your Tests:

Run your tests using the command line: python -m unittest test_simple_calculator.py.

Note for you:
Your goal is to think like a tester and identify as many relevant test cases as possible for each method.
Pay special attention to potential edge cases, such as division by zero, which could lead to unexpected behaviors if not properly handled.
Writing comprehensive tests not only helps ensure your code is working correctly but also improves your understanding of how the code operates under different conditions.
"""
