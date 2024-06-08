# Python Basics

# Introduction
# Python is an interpreted, high-level, general-purpose programming language.
# It was created by Guido van Rossum and first released in 1991.

# Variables and Data Types
# Variables are containers for storing data values.

# Integer
x = 5
print(f"x is an integer: {x}")

# Float
y = 3.14
print(f"y is a float: {y}")

# String
name = "Alice"
print(f"name is a string: {name}")

# Boolean
is_student = True
print(f"is_student is a boolean: {is_student}")

# List
fruits = ["apple", "banana", "cherry"]
print(f"fruits is a list: {fruits}")

# Tuple
coordinates = (10, 20)
print(f"coordinates is a tuple: {coordinates}")

# Dictionary
person = {
    "name": "Alice",
    "age": 25
}
print(f"person is a dictionary: {person}")

# Control Flow

# If Statements
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# For Loop
for fruit in fruits:
    print(fruit)

# While Loop
count = 0
while count < 3:
    print(count)
    count += 1

# Functions

# Defining a Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Functions
add = lambda x, y: x + y
print(add(2, 3))

# Modules
import math
print(math.sqrt(16))

# Error Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution completed.")
