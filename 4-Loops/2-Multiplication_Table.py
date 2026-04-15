"""
For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.
"""

n = int(input("Enter a number: "))

for i in range(1, 11):
    j = i
    power = 0
    while j > 0:
        power += n
        j -= 1
    print(f"{n} * {i} = {power}")
