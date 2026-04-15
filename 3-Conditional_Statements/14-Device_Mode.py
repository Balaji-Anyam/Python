"""
Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"
"""

mode = int(input("Enter a device mode value: "))

if mode == 0:
    print("Standby")
elif mode == 1:
    print("Active")
elif mode == 2:
    print("Fault")
else:
    print("Unknown mode")
