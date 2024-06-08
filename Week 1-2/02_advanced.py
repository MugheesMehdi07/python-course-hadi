# Advanced Python Concepts



# Context Managers
# Context managers allow you to allocate and release resources precisely when you want to.


# Object-Oriented Programming

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

alice = Person("Alice", 25)
alice.greet()

# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())



# Decorators
# Decorators are a way to modify the behavior of a function or method.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Generators
# Generators are functions that return an iterable set of items, one at a time, in a special way.

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# File Handling

# Writing to a File
with open('example.txt', 'w') as file:
    file.write("Hello, World!\nThis is a second line.")

# Reading from a File
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to a File
with open('example.txt', 'a') as file:
    file.write("\nThis is an appended line.")

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())