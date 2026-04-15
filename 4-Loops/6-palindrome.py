"""
Check if the input number reads the same backward as forward, using only loops and arithmetic.
"""

num = int(input("Enter a number: "))

n = num

r = 0

while n > 0:
    r = (r * 10) + (n % 10)
    n = n // 10

if r == num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
