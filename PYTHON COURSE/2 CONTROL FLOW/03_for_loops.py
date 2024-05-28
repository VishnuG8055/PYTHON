# --------------------------------------------
#               FOR LOOPS 🔁
# --------------------------------------------

# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# ---------------- EXAMPLE 1 ----------------

for x in range(1, 11): # end is exclusive # prints 1 - 10
   print(x)

# ---------------- EXAMPLE 2 ----------------

for x in reversed(range(1, 11)):
   print(x)                        # prints 10 - 1

print("Happy New Year!")

# ---------------- EXAMPLE 3 ----------------

for x in range(1, 11, 2):    # step # 1 3 5 7 9
   print(x)                    

# ---------------- EXAMPLE 4 ----------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)                     # Looping Through a String

