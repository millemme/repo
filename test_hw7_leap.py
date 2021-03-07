import unittest
import hw7_leap

class Test_hw7_fizz(unittest.TestCase):
    def test_leap(self):
        result = hw7_leap.leap_year(1)
        self.assertEqual(result, true)
   

if __name__ == '__main__':
    unittest.main()