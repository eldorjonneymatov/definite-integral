import ast
import numpy as np

# define default_functions
default_functions = {
    'np': np,
    'cos': np.cos,
    'sin': np.sin,
    'tan': np.tan,
    'sqrt': np.sqrt,
    'log': np.log,
    'log10': np.log10,
    'exp': np.exp,
    'pow': np.power,
    'asin': np.arcsin,
    'acos': np.arccos,
    'atan': np.arctan,
    'atan2': np.arctan2,
    'ceil': np.ceil,
    'floor': np.floor,
    'fabs': np.fabs,
    'gcd': np.gcd,
    'pi': np.pi,
    'e': np.e,
}


def formula_to_lambda(formula_str):
    """Converts a formula string into a lambda function."""
    # Parse the formula string into an AST (Abstract Syntax Tree)
    formula_ast = ast.parse(formula_str, mode='eval')


    # Check if the AST is a valid expression
    if not isinstance(formula_ast, ast.Expression):
        raise ValueError("Invalid formula expression")

    # Create a lambda function using the AST
    func = lambda x: eval(
        compile(formula_ast, filename='', mode='eval'),
        {'x': x, **default_functions}
    )
    return func


def trapezoidal_rule(f, a, b, n):
    """Approximates the definite integral of f from a to b by the
    composite trapezoidal rule, using n subintervals
    """
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    s = 0.5 * (y[0] + y[-1]) + np.sum(y[1:-1])
    return h * s


def midpoint_rule(f, a, b, n):
    """Approximates the definite integral of f from a to b by the
    midpoint rectangle rule, using n subintervals
    """
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    y = f(x)
    s = np.sum(y)
    return h * s
    

def integrate(f, a, b, n, method='trapezoidal'):
    """Approximates the definite integral of f from a to b by the
    composite trapezoidal rule or midpoint rectangle rule, using n subintervals
    """
    if method == 'trapezoidal':
        return trapezoidal_rule(f, a, b, n)
    elif method == 'midpoint':
        return midpoint_rule(f, a, b, n)
    else:
        raise ValueError("Method must be 'trapezoidal' or 'midpoint'")


def main():
    try:
        # Get formula from user
        formula_str = input("Enter a formula in terms of x: ")
        # Get interval from user
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        n = int(input("Enter n: "))
        print()
        # check if a > b
        if a > b:
            print("a must be less than or equal to b")
            return
        # check if n is positive
        if n <= 0:
            print("n must be positive")
            return
        # Convert formula string to lambda function
        f = formula_to_lambda(formula_str)
        # Calculate the integral using the midpoint rule
        integral = integrate(f, a, b, n, method='midpoint')
        print("Midpoint rule:", integral)
        # Calculate the integral using the trapezoidal rule
        integral = integrate(f, a, b, n, method='trapezoidal')
        print("Trapezoidal rule:", integral)
    except ValueError:
        print("Invalid input for function or interval")
        print("Available functions:")
        print(", ".join(default_functions.keys()))
    except NameError:
        print("Invalid variable in formula, you can only use x")
 

if __name__ == '__main__':
    # Run the main function until the user exits
    while True:
        main()
        print('-' * 80)
        user_input = input("Press q to quit or any other key to continue: ")
        if user_input.lower() == 'q':
            break
        print('-' * 80)