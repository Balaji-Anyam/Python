"""
Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153
"""

for num in range(100, 1000):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
    if num == sum:
        print(num)
