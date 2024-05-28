# -------------------------------
#           COMMENTS
# -------------------------------
# Single-line comment
# This is a single-line comment

# Multi-line comment (Triple-quoted)
"""
This is a multi-line comment
Triple-quoted strings are also used for docstrings,
which are documentation strings for functions, classes, and modules.
"""

# -------------------------------
#           VARIABLES
# -------------------------------
# A variable is a reusable container for storing a value.
# A variable behaves as if it were the value it contains.
age = 4
print(age)
print("You are", age, "years old")

# Concatenation
# String concatenation
print("You are " + str(age) + " years old")

# Separated arguments
print("You are", age, "years old")  # Space between every argument

# f-strings (formatted string literals)
print(f"You are {age} years old")

# DIFFERENT DATA TYPES IN PYTHON

# INTEGER
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT
gpa = 3.2
distance = 2.5
price = 10.9938484673957486784768

print(f"Your GPA is {gpa}")
print(f"You ran {distance} Km")
print(f"The price is ${price:.2f}")  # Formatting float to 2 decimal places

# STRING
name = "Bro"
number = "1"
food = "pizza"
email = "Bro123@gmail.com"

# In Python, there is no char type; single characters are strings of length 1.

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# BOOLEAN
online = True
for_sale = False
running = False

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

# -------------------------------
#     MULTIPLE ASSIGNMENT
# -------------------------------

# Multiple assignment allows you to assign multiple variables at once.
x, y, z = 1, 2, 3
print(x, y, z)

# Multiple variables can be assigned the same value.
x = y = z = 1
print(x, y, z)
