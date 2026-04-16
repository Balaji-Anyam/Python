"""
Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a'
"""

s = str(input("Enter a string: "))
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for i in s:
    if freq[i] == max(freq.values()):
        print("Maximum frequency character:", i)
        break
