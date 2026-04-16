"""
Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes
"""

string = input("Enter a string: ")

is_palindrome = string == string[::-1]

is_symmetrical = (
    len(string) % 2 == 0 and string[: len(string) // 2] == string[len(string) // 2 :]
)

print("Palindrome:", "Yes" if is_palindrome else "No")
print("Symmetrical:", "Yes" if is_symmetrical else "No")
