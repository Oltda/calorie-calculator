
class Calorie:

    '''
    formula: 10 * weight + 6.25 * height - 5 * age + 5 - 10 * temperature

    '''
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        calorie_to_consume = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5 - (10 * self.temperature)
        return calorie_to_consume


my_intake = Calorie(91, 187, 32, 32)
