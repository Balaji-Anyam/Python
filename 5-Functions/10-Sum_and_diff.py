"""
Question: Write a function calculate(a, b) that returns both the sum and difference of a and b.
Sample data:
s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)
Expected output:
Sum: 13
Difference: 7
"""


def calculate(a, b):
    return a + b, a - b


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

s, d = calculate(a, b)

print("Sum:", s)
print("Difference:", d)
