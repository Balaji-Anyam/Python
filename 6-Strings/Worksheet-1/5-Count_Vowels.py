"""
Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5
"""

s = str(input("Enter a string: "))
vowels = set("aeiou")
count = 0

for char in s.lower():
    if char in vowels:
        count += 1

print("Vowels Count:", count)
