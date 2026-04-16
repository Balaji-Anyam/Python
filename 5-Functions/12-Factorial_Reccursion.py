"""
Question: Write a function factorial(n) that uses recursion to calculate the factorial of a number.
Sample data:
print(factorial(5))
Expected output:
120
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number: "))

print(factorial(n))
