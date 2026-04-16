"""
Question: Write a function print_details(name, age) that prints a sentence using both parameters.
Sample data:
print_details("Alice", 25)
Expected output:
Name: Alice, Age: 25
"""

def print_details(name, age):
    print(f"Name: {name}, Age: {age}")  
    
n = str(input("Enter name: "))
a = int(input("Enter age: "))
    
print_details(n, a)
