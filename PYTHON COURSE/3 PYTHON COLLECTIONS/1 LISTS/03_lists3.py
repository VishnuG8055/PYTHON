# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# Python - Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)         # ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)         # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# The length of the list will change when the number of items inserted does not match the number of items replaced.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)         # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)         # ['apple', 'watermelon']

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)         # ['apple', 'banana', 'watermelon', 'cherry']

# Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)         # ['apple', 'banana', 'cherry', 'orange']

# Extend List
# To append elements from another list to the current list, use the extend() method.
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)         # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']    


# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)        # ['apple', 'cherry']

# If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
 