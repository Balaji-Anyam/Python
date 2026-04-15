"""Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
Input: 230
Output: Warning"""

code = int(input("Enter an error code: "))

if code >= 1000:
    print("Critical")
elif code >= 100:
    print("Warning")
elif code < 100:
    print("Info")