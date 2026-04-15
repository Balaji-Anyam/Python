"""Rotate Bits Left by k Positions
Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
Sample Input: n = 150, k = 2"""

n = int(input("Enter a number: "))
k = int(input("Enter a number: "))

print("Result = ", (n << k) | (n >> (32 - k)))
