"""
Check if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes
"""

string = str(input("Enter a string: "))
contains_special_chars = False

for char in string:
    if not char.isalnum():
        contains_special_chars = True
        break

if contains_special_chars:
    print("Contains special character: Yes")
else:
    print("Contains special character: No")
