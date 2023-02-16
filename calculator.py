import re

# Define regular expressions for the operators
bracket_regex = re.compile(r"\((.*?)\)")
operator_high_regex = re.compile(r"\d+[\*\/]\d+")
operator_low_regex = re.compile(r"\d+[\+\-]\d+")
number_regex = re.compile(r"\d+")

# Define the expressions to be evaluated in the eval function
expressions = [bracket_regex, operator_high_regex, operator_low_regex]

def eval(expr):
    # Define the variables
    evaluation = None

    # Remove the brackets if the entire expression is in brackets
    if re.fullmatch(bracket_regex, expr):
        return expr[1:-1]
    
    # Evaluate the expression
    for regex in expressions:
        evaluation = regex.search(expr)
        if evaluation:
            return None if regex.fullmatch(expr) else evaluation
    
    # Return the result
    return evaluation

def calculate(operandA, operator, operandB):
    if operator == "+":
        return int(operandA) + int(operandB)
    elif operator == "-":
        return int(operandA) - int(operandB)
    elif operator == "*":
        return int(operandA) * int(operandB)
    elif operator == "/":
        return int(operandA) / int(operandB)
    else:
        raise Exception("Invalid operator exception")
    
def evaluate(expr):
    # Define the variables
    expr_queue = [expr]
    prev_expr = None
    
    # Start matching pairs
    while True:
        step = eval(expr_queue[-1])

        if step is not None:
            # See if there are more steps to be done
            expr_queue.append(step if type(step) is str else step.group())
        else:
            # Calculate the result
            if number_regex.fullmatch(expr_queue[-1]):
                result = int(expr_queue[-1])
                expr_queue.pop()
            else:
                operandA, operator, operandB = re.match(r"(\d+)([\+\-\*\/])(\d+)", expr_queue[-1]).groups()
                result = calculate(operandA, operator, operandB)

            # Replace until one expression is left
            if prev_expr is not None:
                expr_queue[-2] = expr_queue[-2].replace(prev_expr, str(result))
                prev_expr = expr_queue[-2]
                expr_queue.pop()
            elif len(expr_queue) == 1:
                return result
            else:
                prev_expr = expr_queue[-2]
                expr_queue[-2] = expr_queue[-2].replace(expr_queue[-1], str(result))
                expr_queue.pop()
            
            if len(expr_queue) == 1:
                prev_expr = None