"""Toggle a Specific Bit in an Integer
Given a number and a bit position, write an expression to toggle (flip) that bit.
Sample Input: n = 12, bit_position = 2"""

n = int(input("Enter a number: "))

p = int(input("Enter a bit position: "))

n = n ^ (1 << p)

print("Result = ", n)
