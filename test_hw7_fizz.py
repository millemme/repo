import unittest
import hw7_fizz

class Test_hw7_fizz(unittest.TestCase):
    def test_fizz(self):
        result = hw7_fizz.fizz_buzz(1)
        self.assertEqual(result, 1)
    def test_fizz(self):
        result = hw7_fizz.fizz_buzz(3)
        self.assertEqual(result, "Fizz")

if __name__ == '__main__':
    unittest.main()