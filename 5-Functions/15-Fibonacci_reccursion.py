"""
Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
Sample data:
print(fibonacci(6))
Expected output:
8
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter a number: "))

print(fibonacci(n))
