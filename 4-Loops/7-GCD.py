"""
Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction or division with loops.
"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

while a % b != 0:
    a, b = b, a % b

print("GCD = ", b)
