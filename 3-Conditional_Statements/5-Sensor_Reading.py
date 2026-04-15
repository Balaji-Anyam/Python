"""If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault"""

sen_val = int(input("Enter a sensor value: "))

if sen_val < 100 or sen_val > 900:
    print("Sensor Fault")
else:
    print("Sensor OK")
