from flask import Flask, request, render_template
from calculator.operations import Calculator
from loguru import logger

app = Flask(__name__)
calculator = Calculator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = complex(request.form['num1'])
        num2 = complex(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)

        return render_template('index.html', result=result)
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    logger.add("logs/calculator.log", rotation="10 MB")
    app.run(debug=True)
