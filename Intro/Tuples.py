# Tuples in Python
tuple_ex=("apple", "orange", "kiwi", "banana", "Papaya")
print(tuple_ex) #unchangeable

# Can contain different data types
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))
print(mixed_tuple)  

# Tuple constructor
new_tuple = tuple(("apple", "orange", "kiwi", "banana", "Papaya"))
print(new_tuple)

# Accessing elements
print(tuple_ex[1])

# Changing Tuple elements
# Tuples are immutable, so we cannot change their elements directly
# However, we can create a new tuple by concatenating existing tuples
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
temp_list = list(tuple_ex)
temp_list[1] = "grape"
tuple_ex = tuple(temp_list)
print(tuple_ex)

#for any operations that modify the tuple, we need to convert it to a list first, perform the operation, and then convert it back to a tuple.

#Unpacking tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
my_tuple = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruit1, fruit2, fruit3 = my_tuple
print(fruit1)
print(fruit2)
print(fruit3)   

#Using asterisk* to unpack
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
fruit1, fruit2, *other_fruits = my_tuple
print(fruit1)
print(fruit2)
print(other_fruits)

#index() method
print(tuple_ex.index("kiwi"))   

#count() method
print(tuple_ex.count("kiwi"))

#print the number of items in the tuple
print(len(tuple_ex))



