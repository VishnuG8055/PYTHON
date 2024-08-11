# -------------------------------
#    MATH FUNCTIONS IN PYTHON 📐
# -------------------------------

a = 4
b = 3
c = 5

x = 3.14
y = -4

result = round(x)     # 3
print(result)         # Output: 3
result = round(x, 1)  # 3.1
print(result)         # Output: 3.1
result = abs(y)       # 4
print(result)         # Output: 4

result = pow(a, b)    # 64
print(result)         # Output: 64
result = max(a, b, c) # 5
print(result)         # Output: 5
result = min(a, b, c) # 3
print(result)         # Output: 3

import math

# Constants
print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045

a = 4
b = 2
x = 9.1
result = math.sqrt(a)       # 2.0
print(result)               # Output: 2.0
result = math.pow(a, b)     # 16
print(result)               # Output: 16

result = math.ceil(x)       # 10
print(result)               # Output: 10
result = math.floor(x)      # 9
print(result)               # Output: 9
result = math.factorial(a)  # 24
print(result)               # Output: 24

# Exponential and logarithmic functions
x = 2
print(math.log(x))   # 0.6931471805599453  (Natural logarithm)
print(math.log10(x)) # 0.3010299956639812  (Base-10 logarithm)
print(math.exp(x))   # 7.38905609893065    (Exponential e^x)

# Truncation (removes decimal part)
num = 3.9
print(math.trunc(num))  # 3

# Degrees to radians
degrees = 90
print(math.radians(degrees))  # 1.5707963267948966

# Radians to degrees
radians = math.pi / 2
print(math.degrees(radians))  # 90.0

# Trigonometric functions (input in radians)
angle_radians = math.pi / 4     # 45 degrees

print(math.sin(angle_radians))  # sin(45°) = 0.7071067811865476
print(math.cos(angle_radians))  # cos(45°) = 0.7071067811865476
print(math.tan(angle_radians))  # tan(45°) = 0.9999999999999999
