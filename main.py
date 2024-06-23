from calculator import Calculator
from expression_evaluator import evaluate_expression

def main():
    calculator = Calculator()
    print("Welcome to the command-line calculator!")
    print("Enter expressions like '3 + 4' or '10 / 2'. Type 'quit' to exit.")

    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'quit':
            break
        result = evaluate_expression(expression, calculator)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()