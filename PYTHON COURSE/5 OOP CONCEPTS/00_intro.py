# PYTHON CLASS
# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
# It is a logical entity that contains some attributes and methods. 

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

# SYNTAX
"""
class ClassName:
   Statement-1
   .
   .
   .
   Statement-N
"""

# Class methods = Allow operations related to the class itself
# Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

#---------------------------------------------------------------------------------------------------------------------------------------

class Dog:       # creates a new class named Dog
    pass         # The pass statement is used as a placeholder, meaning the class currently doesn't have any attributes or methods.

# Creating an instance of Dog
my_dog = Dog() 
print(type(my_dog))  # Output: <class '__main__.Dog'>

#-----------------------------------------------------------------------------------------------------------------------------------------

# __init__ method

# The __init__ method in Python is a special method, also known as a constructor.
# It is automatically called when a new instance of a class is created.
# You can use it to initialize the attributes of the class.
# self - reference to the current instance of the class.

class Cat:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing the attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
