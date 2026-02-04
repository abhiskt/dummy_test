class CalculatorError(Exception):
    pass


class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise CalculatorError("Division by zero")
        return a / b

    def add(self, a, b):
        return a + b

    def average(self, numbers):
        if not numbers:
            raise CalculatorError("Empty list")
        return sum(numbers) / len(numbers)

    def is_even(self, number):
        return number % 2 == 0
    

    def is_odd(self, number):
        return not number & 1
