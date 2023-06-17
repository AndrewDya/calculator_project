from loguru import logger

class Calculator:
    def add(self, a, b):
        result = a + b
        logger.info(f"Сложение: {a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        logger.info(f"Умножение: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        try:
            result = a / b
            logger.info(f"Деление: {a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            logger.error("Деление на ноль")
            raise ZeroDivisionError("Деление на ноль")
