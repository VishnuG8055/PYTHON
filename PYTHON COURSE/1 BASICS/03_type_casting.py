#TYPE FUNCTION - type()
name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

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
print(age)
print(type(age))

gpa =3.9999
gpa = int(gpa)
print(gpa)

student = str(student)
print(student)
name = 21
name = bool(name)
print(name)  #True

a = 0
a = bool(a)
print(a)  #False
b = ""
b = bool(b)
print(b)  #False

s = "vishnu"
print(list(s))
print(tuple(s))
print(set(s))

a = 20
print(bin(a))
print(hex(a))
print(oct(a))

# IMPLICIT TYPE CASTING

x = 2
y = 2.5
x = x/y
print(x)
print(type(x))
print(x+y)

a = 5
b = True
print(a+b) # 6