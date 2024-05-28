# Access Items
# List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])     # banana

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])      # cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])     # ['cherry', 'orange', 'kiwi'] end is exclusive

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])      # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])   # ['orange', 'kiwi', 'melon']


# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

list = ["vishnu", 18, "CSBS"]
print("vardhan" in list)          # False