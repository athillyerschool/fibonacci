import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_Three(self):
        result = fibonacci.returnIndexF(3)
        self.assertEqual(result, 2)
    def test_Falc(self):
        result = fibonacci.calcFactorial(7)
        self.assertEqual(result, 5040)
if __name__ == '__main__':
    unittest.main(verbosity=2)
