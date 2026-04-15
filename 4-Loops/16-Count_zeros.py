"""
Input an integer and count how many times 0 appears in it (no strings or lists).
"""

n = int(input("Enter a number: "))

count = 0

while n > 0:
    if n % 10 == 0:
        count += 1
    n //= 10

print("Number of zeros = ", count)
