import argparse
import calculator

# Get the expression from the command line
parser = argparse.ArgumentParser(description='Process a mathematical expression')
parser.add_argument("expression", help="Enter the mathematical expression to be evaluated")
expression = parser.parse_args().expression.replace(" ", "")

# Create the expression queue and the previous expression variable
result = calculator.evaluate(expression)
print(result)