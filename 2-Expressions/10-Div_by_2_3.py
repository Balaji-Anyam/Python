"""Check if a Number is Divisible by Both 2 and 3
Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
Sample Input: num = 18"""

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3")
else:
    print("The number is not divisible by both 2 and 3")