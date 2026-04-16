"""
Question: Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s.
Sample data:
print(string_stats("Hello123"))
Expected output:
(2, 5, 3)
"""


def string_stats(s):
    vowels = 0
    consonants = 0
    digits = 0

    for char in s:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1

    return vowels, consonants, digits


s = str(input("Enter a string: "))

vowels, consonants, digits = string_stats(s)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
