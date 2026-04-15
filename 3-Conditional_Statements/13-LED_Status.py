"""
Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print "All LEDs off".
Input: 0, 1, 0
Output: LED2 ON
"""

led1 = int(input("Enter the status of LED1: "))
led2 = int(input("Enter the status of LED2: "))
led3 = int(input("Enter the status of LED3: "))

if led1 == 1:
    print("LED1 ON")
else:
    print("LED1 OFF")

if led2 == 1:
    print("LED2 ON")
else:
    print("LED2 OFF")

if led3 == 1:
    print("LED3 ON")
else:
    print("LED3 OFF")
