from flask import Flask, request, render_template
from calculator.operations import CalculatorModel, CalculatorView, CalculatorPresenter
from loguru import logger

app = Flask(__name__)
calculator_model = CalculatorModel()
calculator_view = CalculatorView()
calculator_presenter = CalculatorPresenter(calculator_model, calculator_view)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = complex(request.form['num1'])
        operation = request.form['operation']

        if operation in ['add', 'multiply', 'divide']:
            num2 = complex(request.form['num2'])
            result = calculator_presenter.calculate(operation, num1, num2)
        else:
            result = calculator_presenter.calculate(operation, num1)

        history = calculator_model.get_history()

        return render_template('index.html', result=result, history=history)
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    logger.add("logs/calculator.log", rotation="10 MB")
    app.run(debug=True)
