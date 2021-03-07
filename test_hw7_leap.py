import unittest
import hw7_leap

class Test_hw7_fizz(unittest.TestCase):
    def test_leap(self):
        result = hw7_leap.leap_year(1)
        self.assertEqual(result, "no")
    def test_leap(self):
        result = hw7_leap.leap_year(4)
        self.assertEqual(result, "yes")
    def test_leap(self):
        result = hw7_leap.leap_year(100)
        self.assertEqual(result, "no")
    def test_leap(self):
        result = hw7_leap.leap_year(200)
        self.assertEqual(result, "no")
    def test_leap(self):
        result = hw7_leap.leap_year(400)
        self.assertEqual(result, "yes")

   

if __name__ == '__main__':
    unittest.main()