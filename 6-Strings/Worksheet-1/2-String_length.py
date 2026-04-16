"""
Find the Length of a String
Explanation: Count the total characters (including spaces) in a string.
Input: "hello world"
Expected Output: Length: 11
"""

s = str(input("Enter a string: "))
n = 0

for i in s:
    n += 1

print("Length:", n)
