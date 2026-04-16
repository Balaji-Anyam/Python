"""
Question: Write a function area_of_circle(radius) that returns the area (πr²) of a circle for the given radius.
Sample data:
print(area_of_circle(3))
Expected output:
28.274333882308138
"""

def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

r = int(input("Enter the radius of the circle: "))

print(area_of_circle(r))
