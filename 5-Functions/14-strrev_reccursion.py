"""
Question: Write a recursive function reverse_string(s) that returns the reversed string.
Sample data:
print(reverse_string("python"))
Expected output:
nohtyp
"""


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


s = str(input("Enter a string: "))
print("Reversed string:", reverse_string(s))
