"""
Question: Write a function multiply(x, y) that returns the product of its two arguments.
Sample data:
result = multiply(4, 5)
print(result)
Expected output:
20
"""


def multiply(x, y):
    return x * y


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

result = multiply(a, b)
print(result)
