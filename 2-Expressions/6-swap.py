"""Swap Two Numbers Without Using a Third Variable
Swap two variables’ values using a single line of code.
Sample Input: a = 15, b = 8"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

a, b = b, a

print(a,b)