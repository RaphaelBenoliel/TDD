import unittest
from BMI import BMI


class BMITEST(unittest.TestCase):

    def test1(self):
        #Overweight
        weight1 = 150
        height1 = 1.5
        #None
        weight2 = 85
        height2 = 0
        #None
        weight3 = -15
        height3 = 1.56
        #What we expect to receive
        excepted1 = "Overweight"
        excepted2 = "None"
        excepted3 = "None"
        #The result we will get from class BMI
        result1 = BMI.chackBMI(height1, weight1)
        result2 = BMI.chackBMI(height2, weight1)
        result3 = BMI.chackBMI(height3, weight3)

        self.assertEqual(excepted1, result1)  # add assertion here
        self.assertEqual(excepted2, result2)  # add assertion here
        self.assertEqual(excepted3, result3)  # add assertion here

    def test2(self):
        #Underweight
        weight1 = 45
        height1 = 1.6
        #Overweight
        weight2 = 95
        height2 = 1.65
        #A proper weight
        weight3 = 76
        height3 = 1.8
        # What we expect to receive
        excepted1 = "Underweight"
        excepted2 = "Overweight"
        excepted3 = "A proper weight"
        # The result we will get from class BMI
        result1 = BMI.chackBMI(height1, weight1)
        result2 = BMI.chackBMI(height2, weight2)
        result3 = BMI.chackBMI(height3, weight3)

        self.assertEqual(excepted1, result1)
        self.assertEqual(excepted2, result2)
        self.assertEqual(excepted3, result3)


if __name__ == '__main__':
    unittest.main()