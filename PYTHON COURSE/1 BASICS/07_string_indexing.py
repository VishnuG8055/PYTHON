# -------------------------------
#        STRING INDEXING
# -------------------------------
# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]
# starting index - inclusive
# ending index - exclusive

credit_number = "1234-5678-9012-3456"

print(credit_number[0])      # 1
print(credit_number[0:4])    # 1234 (exclusive)
print(credit_number[:4])     # 1234
print(credit_number[4:8])    # -567
print(credit_number[4:])     # -5678-9012-3456
print(credit_number[-1])     # 6 
print(credit_number[-4:])    # 3456
print(credit_number[::2])    # 13-6891-46
print(credit_number[::3])    # 146-136

# -------------------------------
#        EXERCISE
# -------------------------------

# EXERCISE 1
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456

# EXERCISE 2
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)     # 6543-2109-8765-4321 (REVERSE THE STRING)

# PYTHON EMAIL SLICER EXERCISE 📧
email = input("Enter your email: ")

# Ensure there is an '@' character in the email
if '@' in email and email.count('@') == 1:
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print(f"Your username is {username} and domain is {domain}")
else:
    print("Invalid email format.")


import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
