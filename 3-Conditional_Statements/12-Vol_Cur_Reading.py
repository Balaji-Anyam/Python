"""
Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0-3.3V: "Voltage Error"
- Current out of 10-500mA: "Current Error"
- Both out: "Power Error"
"""

voltage = float(input("Enter a voltage reading: "))
current = float(input("Enter a current reading: "))

if voltage < 3.0 or voltage > 3.3:
    print("Voltage Error")
elif current < 10 or current > 500:
    print("Current Error")
else:
    print("Power OK")