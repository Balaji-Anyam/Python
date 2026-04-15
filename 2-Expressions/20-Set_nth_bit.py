"""Set the nth Bit of a Number
Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
Sample Input: n = 9, bit_position = 3"""

n = int(input("Enter a number: "))
p = int(input("Enter a bit position: "))

n = n | (1 << p)

print("Result = ", n)
