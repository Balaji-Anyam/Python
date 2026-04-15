"""
Given a digital input value (0-255), determine and print which of 4 quadrants it falls into: 0-63, 64-127, 128-191, 192-255
"""

value = int(input("Enter a digital input value: "))

if value < 64:
    print("Quadrant 1")
elif value < 128:
    print("Quadrant 2")
elif value < 192:
    print("Quadrant 3")
else:
    print("Quadrant 4")