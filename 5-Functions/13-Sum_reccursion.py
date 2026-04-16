"""
Question: Write a recursive function sum_list(lst) to return the sum of all elements in a list.
Sample data:
print(sum_list([1, 2, 3, 4]))
Expected output:
10
"""


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


n = int(input("Enter a number: "))

l = []

for i in range(n):
    l.append(int(input()))

print("Sum = ", sum_list(l))
