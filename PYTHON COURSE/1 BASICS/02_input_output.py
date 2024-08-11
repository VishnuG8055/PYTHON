# -------------------------------
#            OUTPUT
# -------------------------------
# print() - output function
# every print() call start with new line

print("Hello")
print("welcome","to","python")

# Output -
# Hello
# welcome to python

# end and sep parameters in print()
# end - Customization for continuous output
print("welcome",end =" ")
print("to python")

# Output- 
# welcome to python

# sep - Seperator used between multiple arguments
print("10","08","2004",sep = ".")

# Output - 
# 10.08.2004

# -------------------------------
#             INPUT
# -------------------------------
# input() - This function is used to take input from user
# input() always gives us a string 
# so need to type cast it

name = input("ENTER NAME :")
age = input("Enter age : ")
age = age + 1 

print(age)  # TypeError
print(f"Name : {name}")  

x = int(input("x = "))
y = int(input("y = "))
result = x + y
print("Sum",result)
