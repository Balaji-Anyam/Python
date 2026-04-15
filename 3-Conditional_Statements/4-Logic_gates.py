"""Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to an AND, OR, and XOR gate.
Input: 1, 0
Output: AND: 0, OR: 1, XOR: 1"""

a = int(input("Enter a logic level: "))
b = int(input("Enter another logic level: "))

print("AND:", a and b)
print("OR:", a or b)
print("XOR:", a ^ b)
