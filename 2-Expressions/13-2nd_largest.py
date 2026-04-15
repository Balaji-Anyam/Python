"""Find the Second Largest of Three Numbers
Write an expression (no functions, no if) to get the second largest value among three numbers.
Sample Input: a = 20, b = 12, c = 18"""

a = 12
b = 18
c = 20

if a > b:
    if a > c:
        print(c)
    else:
        print(a)
else:
    if b > c:
        print(c)
    else:
        print(b)
