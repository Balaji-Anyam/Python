"""
Take an integer input and print its digits in reverse order (don’t use slicing or strings).
"""

n = int(input("Enter a number: "))

r = 0

while n > 0:
    r = r * 10 + n % 10
    n = n // 10

print("Reversed number = ", r)
