import unittest
import python_hw4

class Test_python_hw4(unittest.TestCase):
    def test_cube(self):
        result = python_hw4.cube(2)
        self.assertEqual(result, 8)
    def test_cube(self):
        result = python_hw4.cube(-5)
        self.assertEqual(result, -125)
    def test_cube(self):
        result = python_hw4.cube("nice")
        self.assertTrue(result)
    def test_avg(self):
        result = python_hw4.avg([4, 6])
        self.assertEqual(result, 5)
    def test_avg(self):
        result = python_hw4.avg([])
        self.assertException(Exception)
    def test_avg(self):
        result = python_hw4.avg([5, 5, 5])
        self.assertEqual(result, 5)
    def test_combine(self):
        result = python_hw4.combine("Emmet", "Miller")
        self.assertEqual(result, "Emmet Miller")
    def test_combine(self):
        result = python_hw4.combine("Lily", "Naganuma")
        self.assertEqual(result, "Lily Naganuma")
    def test_combine(self):
        result = python_hw4.combine("Ronald", "McDonald")
        self.assertEqual(result, "Ronald McDonald")

if __name__ == '__main__':
    unittest.main()

