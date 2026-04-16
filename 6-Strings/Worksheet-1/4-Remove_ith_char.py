"""
Remove the i-th Character from a String
Explanation: Remove the character at a given index in a string (starting from 0).
Input: String = "Python", i = 2
Expected Output: "Pythn"
"""

s = str(input("Enter a string: "))
i = int(input("Enter the index of the character to remove: "))

print(s[:i] + s[i + 1 :])
