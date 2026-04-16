"""
Question: Write a function greet_person(name, greeting) that prints a personalized message like "Hello, John!" using the arguments.
Sample data:
greet_person("John", "Hi")
Expected output:
Hi, John!
"""

def greet_person(name, greeting):
    print(f"{greeting}, {name}!")
    
n = str(input("Enter name: "))
g = str(input("Enter greeting: "))

greet_person(n, g)
