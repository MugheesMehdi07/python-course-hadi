# Lists, Dictionaries, and File Handling

# Lists
# Lists are used to store multiple items in a single variable.

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list items
print(fruits[0])  # apple

# Modifying list items
fruits[1] = "blueberry"
print(fruits)

# Adding list items
fruits.append("orange")
print(fruits)

# Removing list items
fruits.remove("cherry")
print(fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)

# List Comprehensions
squares = [x ** 2 for x in range(10)]
print(squares)

# Dictionaries
# Dictionaries are used to store data values in key:value pairs.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing dictionary items
print(person["name"])

# Modifying dictionary items
person["age"] = 26
print(person)

# Adding dictionary items
person["email"] = "alice@example.com"
print(person)

# Removing dictionary items
del person["city"]
print(person)

# Looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")


