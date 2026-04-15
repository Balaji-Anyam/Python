"""
Input a number and count how many digits it contains, using only arithmetic and loops.
"""

n = int(input("Enter a number: "))

count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits = ", count)
