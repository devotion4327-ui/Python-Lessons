#Sets   
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates Not Allowed
#Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Get the Length of a Set
#To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#Set Items - Data Types
#Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#Add Items
#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#To add more than one item to a set use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.
#The discard() method will NOT raise an error if the item does not exist.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Join TWO SETS
#There are several ways to join two or more sets in Python. You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.intersection(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set1.intersection_update(set2)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.difference(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set1.difference_update(set2)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.symmetric_difference(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set1.symmetric_difference_update(set2)
print(set1)

#Python Frozenset
#A frozenset is a set that cannot be changed after it is created. A frozenset is immutable, just like a string or a tuple.
#You can create frozenset by using the frozenset() function.    
x = frozenset({"apple", "banana", "cherry"})
print(x)

