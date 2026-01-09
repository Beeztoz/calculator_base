from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self) :
        self.calc = Calculator()

    def test_sum(self) :
        self.assertEqual(self.calc.mysum(1, 2), 3)

    def test_mean(self) :
        self.assertEqual(self.calc.mymean(), 0)
        self.assertEqual(self.calc.mymean(0), 0)
        self.assertEqual(self.calc.mymean(5), 5)
        self.assertEqual(self.calc.mymean(4,6), 5)
        self.assertEqual(self.calc.mymean(1,3), 2)
        self.assertEqual(self.calc.mymean(1,9,2,8,3,7,4,6,5), 5)
        self.assertEqual(self.calc.mymean(-1,0,1), 0)
        self.assertEqual(self.calc.mymean(-1,-9,-2,-8,-3,-7,-4,-6,-5), -5)
        self.assertEqual(self.calc.mymean(1,2), 1.5)

if __name__ == '__main__' :
    unittest.main()
