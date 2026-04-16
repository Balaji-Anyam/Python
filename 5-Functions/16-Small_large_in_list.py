"""
Question: Write a function min_max(numbers) that returns both the smallest and largest number in a list (use returning multiple values).
Sample data:
small, large = min_max([8, 3, 5, 2, 10])
print("Smallest:", small)
print("Largest:", large)
Expected output:
Smallest: 2
Largest: 10
"""


def min_max(numbers):
    return min(numbers), max(numbers)


n = int(input("Enter the number of elements: "))


numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

small, large = min_max(numbers)
print("Smallest:", small)
print("Largest:", large)
