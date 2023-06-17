from loguru import logger
import cmath

class CalculatorModel:
    def __init__(self):
        self.history = []

    def get_history(self):
        return self.history

    def add(self, a, b):
        result = a + b
        logger.info(f"Сложение: {a} + {b} = {result}")
        self.history.append(f"Сложение: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        logger.info(f"Сложение: {a} - {b} = {result}")
        self.history.append(f"Сложение: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        logger.info(f"Умножение: {a} * {b} = {result}")
        self.history.append(f"Умножение: {a} * {b} = {result}")
        return result

    def divide(self, a, b, decimals=2):
        try:
            result = a / b
            real_part = round(result.real, decimals)
            imag_part = round(result.imag, decimals)
            result = complex(real_part, imag_part)
            logger.info(f"Деление: {a} / {b} = {result}")
            self.history.append(f"Деление: {a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            logger.error("Деление на ноль")
            raise ZeroDivisionError("Деление на ноль")

    def square_root(self, a, decimals=2):
        result = cmath.sqrt(a)
        real_part = round(result.real, decimals)
        imag_part = round(result.imag, decimals)
        result = complex(real_part, imag_part)
        logger.info(f"Квадратный корень: sqrt({a}) = {result}")
        self.history.append(f"Квадратный корень: sqrt({a}) = {result}")
        return result

    def power(self, a, b, decimals=2):
        result = cmath.exp(a * cmath.log(b))
        real_part = round(result.real, decimals)
        imag_part = round(result.imag, decimals)
        result = complex(real_part, imag_part)
        logger.info(f"Возведение в степень: {a} ** {b} = {result}")
        self.history.append(f"Возведение в степень: {a} ** {b} = {result}")
        return result


class CalculatorView:
    def display_history(self, history):
        print("История операций:")
        for operation in history:
            print(operation)


class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self, operation, num1, num2=None):
        if operation == "add":
            result = self.model.add(num1, num2)
        elif operation == "subtract":
            result = self.model.subtract(num1, num2)
        elif operation == "multiply":
            result = self.model.multiply(num1, num2)
        elif operation == "divide":
            result = self.model.divide(num1, num2)
        elif operation == "pow":
            result = self.model.power(num1, num2)
        elif operation == "sqrt":
            result = self.model.square_root(num1)
        else:
            raise ValueError("Неподдерживаемая операция")

        return result
