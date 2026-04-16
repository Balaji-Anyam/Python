"""
Question: Write a function is_negative(number) that returns True if the number is negative, else False.
Sample data:
print(is_negative(-7))
print(is_negative(0))
Expected output:
True
False
"""


def is_negative(number):
    return number < 0


n = int(input("Enter a number: "))

print(is_negative(n))
