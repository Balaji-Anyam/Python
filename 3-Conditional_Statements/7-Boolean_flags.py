"""
Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurrent
"""

power_on = True
overcurrent = True
overvoltage = False

if power_on and not overcurrent and not overvoltage:
    print("System Safe")
elif overcurrent:
    print("Shut Down: Overcurrent")
elif overvoltage:
    print("Shut Down: Overvoltage")
else:
    print("Critical Failure")
