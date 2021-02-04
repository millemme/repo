import unittest
import inclass3

if __name__ == '__main__':
    unittest.main()

def test_addition(self):
    result = inclass3.addition(1, 1)
    self.assertEqual(result, 2)

def test_multiplication(self):
    result = inclass3.multiplication(5, 5)
    self.assertEqual(result, 25)

def test_subtraction(self):
    result = inclass3.subtraction(3, 1)
    self.assertEqual(result, 2)

def test_division(self):
    result = inclass3.division(10, 2)
    self.assertEqual(result, 5)