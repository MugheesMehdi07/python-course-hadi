
### 1. Classes and Objects

# class FbUser:
#     username = ""
#     password = ""
#     full_name = ""  #public/private
#
#     def __init__(self, username, password, full_name): #constructor
#         self.username = username
#         self.password = password
#         self.full_name = full_name
#
#     def update_password(self, new_password):
#         self.password = new_password
#
#     def get_user_info(self):
#         return f"Username: {self.username}, Password: {self.password}, Full Name: {self.full_name}"
#
#
# x= FbUser("Mughees", "12345", "Mughees Mehdi")
# y =FbUser("Ali", "12345", "Ali Mehdi")
# z =FbUser("Jawad", "12345", "Jawad Ahmed")
#
# x.username = "Mughees"
# print(x.get_user_info())
# print(y.get_user_info())
#
# x.update_password("new_pass")
# print(x.get_user_info())





# class Dog:
#     # Class attribute
#     species = "Canis familiaris"
#
#     # Initializer / Instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # Instantiate the Dog class
# my_dog = Dog("Buddy", 9)
#
# # Access the instance attributes
# print(f"{my_dog.name} is {my_dog.age} years old.")


### 2. Encapsulation

# class Computer:
#     def __init__(self):
#         self.__max_price = 900  # Private attribute
#
#     def sell(self):
#         print(f"Selling Price: {self.__max_price}")
#
#     def set_max_price(self, price):
#         self.__max_price = price
#
# c = Computer()
# c.sell()
#
# # Try to change the price
# c.__max_price = 1000
# c.sell()
#
# # Using setter function
# c.set_max_price(1000)
# c.sell()

### 3. Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
#
# class Elephant(Animal):
#     def speak(self):
#         return f"{self.name} says Hoo!"
#
# dog = Dog("Max")
# print(dog.speak())
#
# cat = Cat("Felix")
# print(cat.speak())


### 4. Polymorphism


# class India:
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
# class USA:
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
# def describe_country(country):
#     country.capital()
#
# india = India()
# usa = USA()
#
# describe_country(india)
# describe_country(usa)


### 5. Abstraction


# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         pass
#
# class Triangle(Polygon):
#     # overriding abstract method
#     def no_of_sides(self):
#         print("I have 3 sides")
#
# class Pentagon(Polygon):
#     # overriding abstract method
#     def no_of_sides(self):
#         print("I have 5 sides")
#
# # Driver code
# t = Triangle()
# t.no_of_sides()
#
# p = Pentagon()
# p.no_of_sides()


# y = lambda  x : x*x
# print (y(2))


# def sum_ab(a, b):
#   return a + b
# lst = [1,2,3,4,5]
# lst1 = [1,2,3,4,5]
# lst2 = [1,2,3,4,5]
#
#
# x = map(lambda x,y,z : x+y+z, lst, lst1, lst2)
#
# print(list(x))
# for y in x:
#     print(y)



# def my_square(x):
#     return x**x

# def add(a,b):
#     return a+b
#
#
# my_square = lambda x : x**2
#
# add = lambda a,b : a+b
# subt = lambda a,b : a-b
#
#
# print(add(4,5))




#list comprehension

# x = [1,2,3,4]
#
# sq_val = [val ** 2  for val in x  if val > 2 ]
#
# print(sq_val)


# print([x for x in [1,2,3]])
# print([x for x in [1,2,3] if x > 2])
# print([x if x > 2 else 0 for x  in [1,2,3]])

# print(x)
# for i in range(len(x)) :
#     x[i] = x[i] ** 2
#
# print(x)


#Exception Handling:

# x = 10
# y = 2
# try:
#
#     if x < 0 or y < 0:
#         raise Exception("Operand Value should always be positive.")
#
#     print(x / y)
#     print(x * y)
#     print(x + y)
#     print(x - y)
#
# except Exception as e:
#     print(e)
# finally:
#     print("This will run no matter what")


# import Math
#
# Math.pow(2,3)







