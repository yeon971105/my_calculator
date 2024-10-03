# calculator/advanced_operations.py
import math

def power(base, exponent):
    return base ** exponent

def square_root(value):
    if value < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(value)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number")
    return math.factorial(n)


