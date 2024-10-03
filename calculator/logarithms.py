# calculator/logarithms.py
import math

def log(value, base=10):
    if value <= 0:
        raise ValueError("Logarithm only defined for positive values")
    return math.log(value, base)

def natural_log(value):
    if value <= 0:
        raise ValueError("Natural logarithm only defined for positive values")
    return math.log(value)

def exponential(value):
    return math.exp(value)
