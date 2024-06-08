# Strings in Python

# Introduction
# Strings are sequences of characters, used to store text data.
# Strings in Python are immutable, meaning once they are created, they cannot be modified.

# Creating Strings
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, World!"
triple_quote_str = '''This is a
multiline string.'''
print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)

# String Concatenation
# Joining two or more strings together.
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# String Length
# Getting the number of characters in a string.
length = len(full_greeting)
print(f"The length of the greeting is: {length}")

# Accessing Characters
# Strings are indexed, allowing us to access individual characters.
first_char = full_greeting[0]
last_char = full_greeting[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

# Slicing Strings
# Extracting a substring using indices.
substring = full_greeting[0:5]
print(f"Substring: {substring}")

# String Methods
# Common methods for string manipulation.

# upper() and lower()
upper_str = full_greeting.upper()
lower_str = full_greeting.lower()
print(f"Uppercase: {upper_str}")
print(f"Lowercase: {lower_str}")

# strip()
# Removes whitespace from the beginning and end of the string.
whitespace_str = "   Hello, World!   "
stripped_str = whitespace_str.strip()
print(f"Stripped string: '{stripped_str}'")

# replace()
# Replaces a substring with another substring.
replaced_str = full_greeting.replace("Alice", "Bob")
print(f"Replaced string: {replaced_str}")

# split()
# Splits a string into a list of substrings based on a delimiter.
split_str = full_greeting.split(", ")
print(f"Split string: {split_str}")

# join()
# Joins a list of strings into a single string with a specified delimiter.
joined_str = ", ".join(split_str)
print(f"Joined string: {joined_str}")

# find() and rfind()
# Returns the index of the first and last occurrence of a substring.
index_of_Alice = full_greeting.find("Alice")
index_of_last_o = full_greeting.rfind("o")
print(f"Index of 'Alice': {index_of_Alice}")
print(f"Index of last 'o': {index_of_last_o}")

# startswith() and endswith()
# Checks if a string starts or ends with a specified substring.
starts_with_Hello = full_greeting.startswith("Hello")
ends_with_exclamation = full_greeting.endswith("!")
print(f"Starts with 'Hello': {starts_with_Hello}")
print(f"Ends with '!': {ends_with_exclamation}")

# String Formatting
# Using different methods to format strings.

# %-formatting
name = "Alice"
age = 25
formatted_str = "My name is %s and I am %d years old." % (name, age)
print(formatted_str)

# str.format() method
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)

# f-strings (Python 3.6+)
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)

# Escape Characters
# Special characters in strings, starting with a backslash (\).
newline_str = "Hello\nWorld!"
tabbed_str = "Hello\tWorld!"
escaped_quote_str = "He said, \"Hello, World!\""
print(newline_str)
print(tabbed_str)
print(escaped_quote_str)

# String Interpolation
# Embedding expressions inside string literals using f-strings.
expression_str = f"The sum of 2 and 3 is {2 + 3}."
print(expression_str)

# Multiline Strings
# Using triple quotes for strings that span multiple lines.
multiline_str = """This is a string
that spans multiple
lines."""
print(multiline_str)

# Raw Strings
# Treats backslashes as literal characters.
raw_str = r"C:\Users\Alice\Documents"
print(raw_str)

# String Testing Methods
# Checking properties of strings.

# isalpha()
# Returns True if all characters in the string are alphabetic.
alpha_str = "Hello"
print(f"Is alphabetic: {alpha_str.isalpha()}")

# isdigit()
# Returns True if all characters in the string are digits.
digit_str = "12345"
print(f"Is digit: {digit_str.isdigit()}")

# isalnum()
# Returns True if all characters in the string are alphanumeric.
alnum_str = "Hello123"
print(f"Is alphanumeric: {alnum_str.isalnum()}")

# isspace()
# Returns True if all characters in the string are whitespace.
space_str = "   "
print(f"Is whitespace: {space_str.isspace()}")
