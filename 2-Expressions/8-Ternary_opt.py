"""Use the Ternary Operator to Find the Minimum of Two Numbers
Use a single expression to find the smaller of two numbers.
Sample Input: a = 20, b = 13"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("The smaller number is:", a if a < b else b)