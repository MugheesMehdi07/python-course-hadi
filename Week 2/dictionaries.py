# Creating a dictionary
# student = {
#     'name': 'Alice',
#     'age': 20,
#     'major': 'Computer Science',
#     'grades': [85, 92, 88]
# }
#
#
#
#
# print("Student Dictionary:")
# print(student['age'])

# # Output:
# # Student Dictionary:
# # {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'grades': [85, 92, 88]}
#
#
# Accessing dictionary items
# print("Student Name:", student['name'])
# print("Student Age:", student['age'])
# print("Student Major:", student['major'])
# print("Student Grades:", student['grades'])
# #
# # # Output:
# # # Student Name: Alice
# # # Student Age: 20
# # # Student Major: Computer Science
# # # Student Grades: [85, 92, 88]
# #
# #
# # # Adding and modifying dictionary items
# student['email'] = 'alice@example.com'  # Adding a new key-value pair
# student['age'] = 21  # Modifying the 'age' value
# #
# print("Updated Student Dictionary:")
# print(student)
#
# # Output:
# # Updated Student Dictionary:
# # {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grades': [85, 92, 88], 'email': 'alice@example.com'}
#
#
# # Iterating through a dictionary
# print("Student Information:")
# for key, value in student.items():
#     print(key + ":", value)
#
# for value in student.values():
#     print("Values" , value)
#
# for key in student:
#     print("Keys" , key)


#
# # Output:
# # Student Information:
# # name: Alice
# # age: 21
# # major: Computer Science
# # grades: [85, 92, 88]
# # email: alice@example.com
#
#
# # Dictionary comprehension
squared_numbers = {x: x*x for x in range(1, 6)}
print(squared_numbers)


#
# print("Squared Numbers Dictionary:")
# print(squared_numbers)
#
# # Output:
# # Squared Numbers Dictionary:
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
