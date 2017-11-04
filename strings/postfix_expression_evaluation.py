# http://www.ideserve.co.in/learn/postfix-expression-evaluation

OPERATORS = ["+", "-", "/", "*"]


def postfix_expression_evalutaion(values):
    idx = 0
    while len(values) > 2:
        if (values[idx]) in OPERATORS:
            expression = "{0} {2} {1}".format(*(values[idx - 2:idx+1]))
            result = eval(expression)
            values = [*values[0:idx-2], str(result), *values[idx+1:len(values)]]
            idx = 0
        idx += 1

    return values[0] if len(values) == 1 else "invalid input"


if __name__ == "__main__":
    values = ['5', '1', '2', '+', '4', '*', '+', '3', '-']
    print("value of the expression: ", postfix_expression_evalutaion(values))
