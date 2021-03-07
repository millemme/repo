import unittest
import hw7_fizz

class Test_hw7_fizz(unittest.TestCase):
    def test_fizz(self):
        result = hwy_fizz.fizz_buzz(1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()