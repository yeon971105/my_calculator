# calculator/complex_numbers.py
def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def divide_complex(c1, c2):
    if c2 == 0:
        raise ValueError("Cannot divide by zero")
    return c1 / c2
