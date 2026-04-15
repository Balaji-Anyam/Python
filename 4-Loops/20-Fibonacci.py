"""
Input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion).
"""

n = int(input("Enter a number: "))

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print("Fibonacci number = ", a)
