from decorators import error_handling_decorator
from calculator import calculator

@error_handling_decorator
def expression(expression, calculator):
    try:
        a, operator, b = expression.split()
        a, b = float(a), float(b)
    except Exception as e:
        print(e)

    if operator == '+':
        return calculator.add(a, b)
    elif operator == '-':
        return calculator.subtract(a, b)
    elif operator == '*':
        return calculator.multiply(a, b)
    elif operator == '/':
        return calculator.divide(a, b)
    else:
        raise ValueError("Unknown operator")