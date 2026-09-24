import unittest
from main import equalisation

class Test_rashala(unittest.TestCase):

    def test_calculation_ok(self):
        self.assertEqual((1, 7, 5, 3, 9), 7.0)  
    
    def test_calculation_05ok(self):
        self.assertEqual(equalisation(2, '54', 5, '4', 9), 9.0)

    def test_div_by_zero(self):
        self.assertEqual(equalisation(1, 2, 5, 5, 16), "На ноль делить нельзя")

    def test_wrong_type(self):
        self.assertEqual(equalisation("fwesdf", 2, 3, 4, 5), "Вы задали не тот тип данных")

if __name__ == '__main__':
    unittest.main()
