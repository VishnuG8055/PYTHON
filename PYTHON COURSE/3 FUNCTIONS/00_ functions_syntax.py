# Python Functions: An Enhanced Guide

# Basics of Functions
# --------------------
# In Python, a function is a reusable block of code that only runs when it is called. 
# Functions help in organizing code, reducing repetition, and improving readability.

# Defining a Function
def my_function():
    """
    This function prints a greeting message.
    """
    print("Hello")

# Calling a Function
my_function()  # Output: Hello

# Functions with Arguments
# -------------------------
# Functions can take inputs known as arguments. These allow you to pass data to the function when calling it.

# Example
Name = "Vishnu"
roll = 810

def Student(name, roll_number):
    """
    Prints the student's name and roll number.
    """
    print(f"Your Name is {name} and roll number is {roll_number}")

Student(Name, roll)  # Output: Your Name is Vishnu and roll number is 810

# Functions with Return Values
# -----------------------------
# A function can return a value using the `return` keyword. This allows you to use the result of the function elsewhere in your code.

# Example
def sum(a, b):
    """
    Returns the sum of two numbers.
    """
    total = a + b
    return total

a = 1
b = 4
result = sum(a, b)
print(f"Sum of {a} and {b} is {result}")  # Output: Sum of 1 and 4 is 5

# Default Arguments
# ------------------
# Functions can have default arguments, which are used if no argument is provided during the function call.

# Example
def fun(name="Vishnu"):
    """
    Prints a message including the name. Defaults to "Vishnu" if no name is provided.
    """
    print(f"{name} is GREAT")

fun()             # Output: Vishnu is GREAT
fun("Virat")      # Output: Virat is GREAT

# Keyword Arguments
# ------------------
# You can specify arguments by name, allowing you to pass them in any order.

# Example
def greet(name, message="Hello"):
    """
    Prints a greeting message with the provided name. Defaults to "Hello" if no message is provided.
    """
    print(f"{message}, {name}!")

greet("Alice", message="Good morning")  # Output: Good morning, Alice!
greet(name="Bob")                       # Output: Hello, Bob!

# Variable-Length Arguments
# --------------------------
# Python allows functions to accept an arbitrary number of arguments using *args for positional arguments and **kwargs for keyword arguments.
# args = ARuGumentS
# kwargs = KeyWord ARGumentS

# Example
def my_function(*args, **kwargs):
    """
    Prints all positional arguments and keyword arguments provided to the function.
    """
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, a=4, b=5)
# Output:
# Arguments: (1, 2, 3)
# Keyword arguments: {'a': 4, 'b': 5}

# Best Practices
# ---------------
# 1. Naming Conventions: Use descriptive names for functions and variables to make your code readable.
#    Example: `calculate_sum` is more descriptive than `sum`.

# 2. Docstrings: Include a docstring (a string literal) immediately after the function definition to describe what the function does.

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

# 3. Avoid Global Variables: Minimize the use of global variables inside functions. Pass variables as arguments instead.

# 4. Keep Functions Focused: Each function should perform a single task. This makes it easier to understand, test, and reuse.

# 5. Handle Exceptions: Consider using try-except blocks inside functions to handle potential errors gracefully.

def divide(a, b):
    """
    Returns the result of dividing a by b. Handles division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# Example Usage
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero!


# Nested Functions
# -----------------
# Functions can be defined inside other functions. These are called nested functions or inner functions.

# Example
def outer_function(x):
    """
    An outer function that calls an inner function.
    """
    def inner_function(y):
        """
        An inner function that returns the square of y.
        """
        return y * y
    return inner_function(x) + 10

print(outer_function(5))  # Output: 35

# Lambda Functions
# -----------------
# Lambda functions are small anonymous functions defined with the lambda keyword.

# Example
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Function Annotations
# ---------------------
# Function annotations are a way to attach metadata to function arguments and return values.

# Example
def greet(name: str, age: int) -> str:
    """
    Returns a greeting message including the name and age.
    """
    return f"Hello {name}, you are {age} years old."

print(greet("Alice", 30))  # Output: Hello Alice, you are 30 years old.

# Higher-Order Functions
# -----------------------
# Higher-order functions are functions that take other functions as arguments or return functions as results.

# Example
def apply_function(func, value):
    """
    Applies a function to a value.
    """
    return func(value)

def square(x):
    """
    Returns the square of x.
    """
    return x * x

print(apply_function(square, 4))  # Output: 16

# Decorators
# ----------
# Decorators are a way to modify or extend the behavior of functions without changing their code.

# Example
def decorator_function(func):
    """
    A decorator that wraps the provided function with additional behavior.
    """
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator_function
def say_hello():
    """
    A simple function that prints a hello message.
    """
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Function Scope and Lifetime
# ---------------------------
# Local variables are only accessible within the function they are defined in, while global variables are accessible throughout the module.

# Example
def my_function():
    """
    Demonstrates function scope.
    """
    local_var = 10
    print(local_var)  # Output: 10

my_function()
# print(local_var)  # This would raise an error as local_var is not defined outside my_function.

# Recursion
# ---------
# A function that calls itself is known as a recursive function. It requires a base case to terminate the recursion.

# Example
def factorial(n):
    """
    Returns the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Closures
# --------
# A closure occurs when a nested function references a value from its enclosing scope.

# Example
def make_multiplier(multiplier):
    """
    Returns a function that multiplies its input by the given multiplier.
    """
    def multiply(number):
        return number * multiplier
    return multiply

times_two = make_multiplier(2)
print(times_two(5))  # Output: 10

# Best Practices
# ---------------
# 1. Naming Conventions: Use descriptive names for functions and variables to make your code readable.
#    Example: `calculate_sum` is more descriptive than `sum`.

# 2. Docstrings: Include a docstring (a string literal) immediately after the function definition to describe what the function does.

# Example
def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

# 3. Avoid Global Variables: Minimize the use of global variables inside functions. Pass variables as arguments instead.

# 4. Keep Functions Focused: Each function should perform a single task. This makes it easier to understand, test, and reuse.

# 5. Handle Exceptions: Consider using try-except blocks inside functions to handle potential errors gracefully.

# Example
def divide(a, b):
    """
    Returns the result of dividing a by b. Handles division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero!
