"""
Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary
"""

import random
import string

target_string = str(input("Enter the target string: "))
attempts = 0

while True:
    random_string = "".join(random.choices(string.ascii_letters, k=len(target_string)))
    attempts += 1

    if random_string == target_string:
        break

print(f"Randomly generated '{target_string}' after {attempts} attempts.")
