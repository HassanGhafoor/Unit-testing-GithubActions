# calculator.py
# Making any change

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, or an error message if dividing by zero."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

