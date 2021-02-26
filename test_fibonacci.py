import unittest
import fibonacci

def test_fibs(self):
    result = fibonacci.fibs(1)
    self.assertEqual(result, 0)
    result = fibonacci.fibs(3)
    self.assertEqual(result, [0,1,1])
    
def test_factorial(self):
    result = fibonacci.factorial(1)
    self.assertEqual(result, 1)
    result = fibonacci.factorial(5)
    self.assertEqual(result, 120)
    
if __name__ == '__main__':
    unittest.main()
