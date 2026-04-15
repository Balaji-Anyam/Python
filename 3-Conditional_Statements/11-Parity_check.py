"""
Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even
"""

val = int(input("Enter a 16-bit value: "), 16)

if val % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")
