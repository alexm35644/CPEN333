from demo import Arithmetic
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.arithmetic = Arithmetic()

    def test_add(self):
        result = self.arithmetic.add(4, 7)
        self.assertEqual(result, 11)

    def test_subtract(self):
        result = self.arithmetic.subtract(6, 3)
        self.assertEqual(result, 3) #yo this fails

    def test_add2(self):
        result = self.arithmetic.add(11, 900)
        self.assertEqual(result, 911)

    def test_subtract2(self):
        result = self.arithmetic.subtract(21, 11)
        self.assertEqual(result, 11) #yo this works

if __name__ == '__main__':
    unittest.main()
