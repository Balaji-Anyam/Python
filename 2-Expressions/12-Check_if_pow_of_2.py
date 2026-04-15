"""Check if a Number is a Power of Two
Write a single Boolean expression to check if a number is a power of two.
Sample Input: n = 32"""

a = int(input("Enter a number: "))


if a & (a - 1) == 0:
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")
