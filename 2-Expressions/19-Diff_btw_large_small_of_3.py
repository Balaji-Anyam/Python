"""Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
Write an expression to find the difference between the largest and the smallest of three numbers.
Sample Input: a = 8, b = 27, c = 14"""

a = 8
b = 27
c = 14

max = a * (a > b and a > c) + b * (b > a and b > c) + c * (c > a and c > b)
min = a * (a < b and a < c) + b * (b < a and b < c) + c * (c < a and c < b)

print("Difference = ",max - min)