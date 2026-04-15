"""Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set"""

reg_val = int(input("Enter a 8-bit register value: "))

if reg_val & 128 == 128:
    print("MSB set")
else:
    print("MSB not set")