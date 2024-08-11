#TYPE FUNCTION - type()
name = "Vishnu"
age = 20
gpa = 9.4
student = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(gpa))      # <class 'float'>
print(type(student))  # <class 'bool'>

# -------------------------------
#         TYPE CASTING
# -------------------------------
# TYPE CASTING = The process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit
# Explicit type casting requires manual intervention
# Implicit type casting is handled automatically by the compiler

# EXPLICIT TYPE CASTING
age = 21
age = float(age)  
print(age)         # 21.0
print(type(age))   # <class 'float'>

gpa = 9.9999
gpa = int(gpa)
print(gpa)          # 9

student = True
student = str(student) 
print(student)      # True
age = 21
age = bool(age)
print(age)         # True

a = 0
a = bool(a)
print(a)      # False
b = ""
b = bool(b)
print(b)      # False

s = "vishnu"
print(list(s))
print(tuple(s))
print(set(s))

# Output- 
# ['v', 'i', 's', 'h', 'n', 'u']
# ('v', 'i', 's', 'h', 'n', 'u')
# {'u', 'h', 'n', 'i', 's', 'v'}

a = 20
print(bin(a))
print(hex(a))
print(oct(a))

# Ouput- 
# 0b10100
# 0x14
# 0o24

#---------------------------
# IMPLICIT TYPE CASTING
#---------------------------

x = 2
y = 2.5
z = 3
x = x/y           # Since y is a float, the result of the division will be a float
print(x)          # 0.8
print(type(x))    # <class 'float'>
print(z+y)        # 5.5

a = 5
b = True
print(a+b) # 6


#-------------------------
