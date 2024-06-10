# Python Basics

# Introduction
# Python is an interpreted, high-level, general-purpose programming language.
# It was created by Guido van Rossum and first released in 1991.
# Python is known for its easy-to-read syntax, versatility, and wide range of applications.

# Variables and Data Types
# Variables are containers for storing data values.
# Python is dynamically typed, meaning you don't need to declare the type of a variable.

# Integer
x = 5
print(f"x is an integer: {x}")  # Output: x is an integer: 5

# You can perform arithmetic operations with integers.
a = 10
b = 3
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
quot_ab = a / b  # Division results in a float
int_div_ab = a // b  # Integer division
mod_ab = a % b  # Modulus operation

print(f"Sum: {sum_ab}, Difference: {diff_ab}, Product: {prod_ab}, Quotient: {quot_ab}, Integer Division: {int_div_ab}, Modulus: {mod_ab}")

# Float
y = 3.14
print(f"y is a float: {y}")  # Output: y is a float: 3.14

# Floats are used for decimal and fractional numbers.
float_div = a / b
print(f"Division resulting in float: {float_div}")

# String
name = "Alice"
print(f"name is a string: {name}")  # Output: name is a string: Alice

# Strings can be concatenated and repeated.
greeting = "Hello, " + name + "!"
repeated_name = name * 3
print(greeting)  # Output: Hello, Alice!
print(repeated_name)  # Output: AliceAliceAlice

# Boolean
is_student = True
print(f"is_student is a boolean: {is_student}")  # Output: is_student is a boolean: True

# Booleans are used for conditional statements and can be combined with logical operators.
has_access = is_student and age >= 18
print(f"Has access: {has_access}")  # Output: Has access: True

# List
fruits = ["apple", "banana", "cherry"]
print(f"fruits is a list: {fruits}")  # Output: fruits is a list: ['apple', 'banana', 'cherry']

# Lists are ordered, mutable collections of items.
fruits.append("orange")
fruits.remove("banana")
first_fruit = fruits[0]
last_fruit = fruits[-1]
print(f"Updated fruits list: {fruits}")  # Output: Updated fruits list: ['apple', 'cherry', 'orange']
print(f"First fruit: {first_fruit}, Last fruit: {last_fruit}")  # Output: First fruit: apple, Last fruit: orange

# Tuple
coordinates = (10, 20)
print(f"coordinates is a tuple: {coordinates}")  # Output: coordinates is a tuple: (10, 20)

# Tuples are ordered, immutable collections of items.
# They are often used for fixed collections of related items.
x_coord, y_coord = coordinates
print(f"x coordinate: {x_coord}, y coordinate: {y_coord}")  # Output: x coordinate: 10, y coordinate: 20

# Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"person is a dictionary: {person}")  # Output: person is a dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Dictionaries are collections of key-value pairs.
# They are unordered and mutable.
person["email"] = "alice@example.com"
del person["city"]
print(f"Updated person dictionary: {person}")  # Output: Updated person dictionary: {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

# Control Flow

# If Statements
age = 20
if age >= 18:
    print("You are an adult.")  # Output: You are an adult.
else:
    print("You are a minor.")

# You can use elif for multiple conditions.
temperature = 30
if temperature > 30:
    print("It's hot outside.")
elif temperature < 10:
    print("It's cold outside.")
else:
    print("The weather is moderate.")  # Output: The weather is moderate.

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# You can use the range() function to iterate over a sequence of numbers.
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# While Loop
count = 0
while count < 3:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2

# Functions

# Defining a Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Functions can have multiple parameters and default values.
def introduce(name, age, city="Unknown"):
    return f"My name is {name}, I am {age} years old, and I live in {city}."

print(introduce("Alice", 25, "New York"))  # Output: My name is Alice, I am 25 years old, and I live in New York.
print(introduce("Bob", 30))  # Output: My name is Bob, I am 30 years old, and I live in Unknown.

# Lambda Functions
# Lambda functions are small anonymous functions defined with the lambda keyword.

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Lambda functions are often used for short, throwaway functions.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Modules
# Modules are files containing Python code that can be imported into other Python files.
# The math module provides mathematical functions.

import math
print(math.sqrt(16))  # Output: 4.0

# You can also import specific functions from a module.
from math import pow
print(pow(2, 3))  # Output: 8.0

# Error Handling
# Error handling allows you to manage errors in a program without crashing.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")  # Output: Cannot divide by zero.
finally:
    print("Execution completed.")  # Output: Execution completed.

# You can handle multiple exceptions using multiple except blocks.
try:
    num = int("abc")
except ValueError:
    print("Invalid input. Please enter a number.")  # Output: Invalid input. Please enter a number.
except ZeroDivisionError:
    print("Cannot divide by zero.")
