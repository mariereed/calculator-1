"""Math functions for calculator."""
from __future__ import division

def add(num1, num2):
    """Return the sum of the two inputs."""

    return (float(num1) + num2)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return (float(num1) - num2)

def multiply(num1, num2):
    """Multiply the two inputs together."""

    return (float(num1) * num2)

def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return (float(num1) / num2)

def square(num1):
    """Return the square of the input."""

    return (float(num1) ** 2)

def cube(num1):
    """Return the cube of the input."""
 
    return (float(num1) ** 3)

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return (float(num1) ** num2)

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return (float(num1) % num2)

def add_mult(num1, num2, num3):
    return (int((num1+num2)*num3))

def add_cubes(num1, num2):
    return int((num1**3 + num2**3))