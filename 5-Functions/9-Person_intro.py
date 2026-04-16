"""
Question: Write a function introduction(name, country='India') that prints a message introducing the person and their country.
Sample data:
introduction("Sara")
introduction("Alex", "USA")
Expected output:
My name is Sara and I am from India.
My name is Alex and I am from USA.
"""

def introduction(name, country='India'):
    print(f"My name is {name} and I am from {country}.")
    
n = str(input("Enter name: "))
c = str(input("Enter country: "))

introduction(n, c)
