"""
Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
"""

a = int(input("Enter a reading: "))
b = int(input("Enter another reading: "))

if abs(a - b) <= 5:
    print("Match")
else:
    print("No Match")
