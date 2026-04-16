"""
Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin"
"""

s = str(input("Enter a string: "))

s = "".join(set(s))

print(s)
