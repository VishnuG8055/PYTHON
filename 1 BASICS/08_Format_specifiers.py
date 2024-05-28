# -------------------------------
#       FORMAT SPECIFIERS
# -------------------------------

# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3.14159
price2 = -987.65

# DECIMAL PRECISION
print(f"price1 is: ${price1:.3f}") # $3.142
print(f"price2 is: ${price2:.1f}") # $-987.6

# PADDING
print(f"price1 is: ${price1:10}") # $   3.14159
print(f"price2 is: ${price2:10}") # $   -987.65

# ZERO PADDING
print(f"price1 is: ${price1:010}") # $0003.14159
print(f"price2 is: ${price2:010}") # $-000987.65

# LEFT JUSTIFY
print(f"price1 is: ${price1:<10}") # $3.14159 
print(f"price2 is: ${price2:<10}") # $-987.65

# RIGHT JUSTIFY
print(f"price1 is: ${price1:>10}") # $   3.14159
print(f"price2 is: ${price2:>10}") # $   -987.65

# CENTER ALIGN
print(f"price1 is: ${price1:^10}") # $ 3.14159
print(f"price2 is: ${price2:^10}") # $ -987.65

# POSITIVE VALUES
print(f"price1 is: ${price1:+}") # $+3.14159
print(f"price2 is: ${price2:+}") # $-987.65

# SPACE FOR POSITIVE VALUES
print(f"price1 is: ${price1: }") # $ 3.14159
print(f"price2 is: ${price2: }") # $-987.65

a = 1234.75
b = -5365.7866

# COMMA SEPARATOR
print(f"{a:,}") # 1,234.75
print(f"{b:,}") # -5,365.7866

# MULTIPLE 
print(f"{a:+,.2f}") # +1,234.75
print(f"{b:+,.2f}") # -5,365.78

# PERCENTAGE FORMAT
print(f"{a:%}") # 123475.000000%
print(f"{b:%}") # -536578.660000%