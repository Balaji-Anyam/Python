"""
Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes
"""

string = input("Enter a string: ")
is_binary = all(char in "01" for char in string)

print("Is binary string:", "Yes" if is_binary else "No")
