"""
Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']
"""

list_of_words = ["apply", "apples", "ape", "maple"]
target_word = "apple"

close_matches = []

for word in list_of_words:
    distance = sum(1 for a, b in zip(word, target_word) if a != b)
    if distance <= 2:
        close_matches.append(word)

print("Close matches:", close_matches)
