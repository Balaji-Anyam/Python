"""
Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.
"""

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
