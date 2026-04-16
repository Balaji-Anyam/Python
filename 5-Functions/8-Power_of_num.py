"""
Question: Write a function power(base, exponent=2) that returns base raised to exponent (default is square).
Sample data:
print(power(3))
print(power(2, 5))
Expected output:
9
32
"""

def power(base, exponent=2):
    return base ** exponent

b = int(input("Enter a base number: "))
e = int(input("Enter an exponent number: "))

print(power(b, e))
