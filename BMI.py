class BMI:
    weight = 0
    height = 0

    def calcBmi(height, weight):
        """if height == 0:
            return None"""
        if weight <= 0 or height <= 0:
            return None
        else:
            return weight / (height ** 2)

    def chackBMI(height, weight):
        bmi = BMI.calcBmi(height, weight)
        if bmi is None:
            return "None"
        if bmi > 25:
            return "Overweight"
        if bmi < 18.5:
            return "Underweight"
        else:
            return "A proper weight"
