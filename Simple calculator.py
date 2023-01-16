class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def product(self):
        return self.first * self.second

    def division(self):
        if self.second != 0:
            return self.first / self.second
        else:
            return "Division by zero is not allowed"


calculator = Calculator(2, 0)
print(calculator.division())

