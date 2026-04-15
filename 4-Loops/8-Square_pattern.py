"""
Print a hollow square pattern of size n (n ≥ 3).
Example for n = 5:
*****
*   *
*   *
*   *
*****
"""

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
