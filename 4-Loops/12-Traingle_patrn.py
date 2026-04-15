"""
For n rows, print a right-aligned triangle pattern:
    *
   **
  ***
 ****
*****
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
