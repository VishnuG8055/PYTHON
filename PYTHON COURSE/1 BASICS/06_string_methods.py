# -------------------------------
# STRING METHODS
# -------------------------------
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

length = len(name)        # counts spaces too
index = name.find(" ")    # Gives index of first occurence of given char
index = name.rfind(" ")   # Gives index of last occurence of given char r means reverse
# if given a char which is not present in string then it gives -1

name = name.capitalize()  # Converts the first character of the string to uppercase and the rest to lowercase
name = name.upper()       # Converts all characters in the string to uppercase
name = name.lower()       # Converts all characters in the string to lowercase
name = name.title()       # Converts the first character of each word to uppercase and the rest to lowercase
result = name.isdigit()   # returns True if only string contains all digits else False
result = name.isalpha()   # returns True if only string contains all alphabets else False even if space it is False
result = phone_number.count("-")  # Returns the number of occurrences of a substring in the string
phone_number = phone_number.replace("-", "") # replace(old, new): Replaces all occurrences of the old substring with the new substring.

print(help(str))   # Gives list of string methods

# -------------------------------
#        EXERCISE
# -------------------------------

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif " " in username:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")



# -------------------------------
#       ESCAPE CHARACTER
# -------------------------------

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."   (ERROR)
txt = "We are the so-called \"Vikings\" from the north."   #(corrected with escape char)
