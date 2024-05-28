# -------------------------------
#      OPERATORS IN PYTHON
# -------------------------------

# -------------------------------
#      AIRTHMETIC OPERATORS
# -------------------------------
a = 1
b = 2
result = a + b   # (+)  ADDITION OPERATOR
result = a - b   # (-)  SUBTRACTION OPERATOR
result = a * b   # (*)  MULTIPLICATION OPERATOR
result = a / b   # (/)  DIVISION OPERATOR (True division resulting decimal)
result = a // b  # (//) FLOOR DIVISION OPERATOR (Integer Division rounding to nearest smallest integer)(Quotient)
result = a % b   # (%)  MODULUS OPERATOR (Remainder)
result = a ** b   # (**) EXPONENTIATION OPERATOR

# -------------------------------
#      ASSIGNMENT OPERATORS
# -------------------------------

# SIMPLE ASSIGNMENT (=) Assigns a value to a variable
x = 10
y = 20

# AUGMENTED ASSIGNMENT
x += 1  # Equivalent to: x = x + 1
x -= 1  # Equivalent to: x = x - 1
x *= 2  # Equivalent to: x = x * 2
x /= 2  # Equivalent to: x = x / 2
x //= 2 # Equivalent to: x = x // 2
x %= 2  # Equivalent to: x = x % 2
x **= 2 # Equivalent to: x = x ** 2


# -------------------------------
#      COMPARISION OPERATORS 
# -------------------------------
#( all returns True)
x == y  # Equal to
x != y  # Not equal to
x > y   # Greater than
x < y   # Less than
x >= y  # Greater than or equal to
x <= y  # Less than or equal to

# -------------------------------
#       LOGICAL OPERATORS
# -------------------------------
x = True
y = False

# Logical AND
print(x and y)  # False

# Logical OR
print(x or y)   # True

# Logical NOT
print(not x)    # False
print(not y)    # True


# -------------------------------
#       BITWISE OPERATORS
# -------------------------------
# Bitwise AND: &
# Bitwise OR: |
# Bitwise XOR: ^
# Bitwise NOT: ~
# Left Shift: <<
# Right Shift: >> (Shifts the bits of the no.to right)(Fills 1 in case of Negative no.)

a = 3 # 0011
b = 4 # 0100
print(a&b)  # 0000 # output 0
print(a|b)  # 0111 # output 7
print(a^b)  # 0111 # output 7
print(~a)   # 1100 # output -4
print(a<<1) # 0110 # output 6
print(a>>1) # 0001 # output 1

# Bitwise Operator Overloading

# Membership Operators

# Identity Operators

