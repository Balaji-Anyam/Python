"""
Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a'
"""

s = str(input("Enter a string: "))
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for i in s:
    if freq[i] == min(freq.values()):
        print("Least frequent character:", i)
        break
