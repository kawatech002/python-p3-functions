#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

# Call the function to see the output
greet_programmer()

def greet(name):
    print("Hello, " + name + "!")

# Call the function with a specific name
greet("John")


def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

# Call the function without specifying a name (uses the default)
greet_with_default()

# Call the function with a specific name
greet_with_default("John")


def add(num1, num2):
    return num1 + num2

# Example usage:
result = add(3, 7)
print(result)  # Output: 10

def halve(number):
    return number / 2

# Example usage:
result = halve(8)
print(result)  # Output: 4.0

