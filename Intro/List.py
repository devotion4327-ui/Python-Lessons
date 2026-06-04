# Lists in Python
my_list = [1, 2, 3, 4, 5]
print(my_list)  
# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
# Modifying elements
my_list[1] = 20
print(my_list)
# Adding elements
my_list.append(6)
print(my_list)
# Removing elements
my_list.remove(3)
print(my_list)
# Slicing lists
print(my_list[1:4])  # Output: [20, 4, 5]
# Length of the list
print(len(my_list))  # Output: 5
# Iterating through the list
for item in my_list:
    print(item)
# List comprehension
squared = [x**2 for x in my_list]
print(squared)  # Output: [1, 400, 16, 25
# Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2] 
print(nested_list[1][0])  # Output: 3
# List methods
my_list.sort()
print(my_list)  # Output: [1, 4, 5, 6, 20]
my_list.reverse()
print(my_list)  # Output: [20, 6, 5, 4, 1]
my_list.clear()
print(my_list)  # Output: []
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4
# 5, 6] 
repeated = list1 * 3
print(repeated)  # Output: [1, 2, 3, 1
# 2, 3, 1, 2, 3]
#List Length
print(len(list1))  # Output: 3

#Type of List
print(type(list1))  # Output: <class 'list'>    

#List Construction
new_list = list((7, 8, 9))
print(new_list)  # Output: [7, 8, 9]    

#TESTING
newlist= list(("apple", "orange", "kiwi", "banana", "Papaya"))
print(newlist[-4: -1])

if "Papaya" in newlist:
    print("yes")

#To change the range of iteam values in the list
newlist[3: 1] = ["grape", "mango"]
print(newlist)

#To insert a new item in the list
newlist.insert(3, "Jack fruit")
print(newlist)

#To add an item to the end of the list
newlist.append("Watermelon")
print(newlist)

#Extend the list by adding all the items from another list
tropical = ["Pineapple", "Coconut"]
newlist.extend(tropical)
print(newlist)

#Remove an item from the list
newlist.remove("Jack fruit")
print(newlist)

#Remove specified index
newlist.pop(2)
print(newlist)

del newlist[0]
print(newlist)

#Clear the list
my_list.clear()
print(my_list)

#Looping through a list
for x in newlist:
    print(x)

for i in range(len(newlist)-2):
    print(newlist[i])

#While loop
j = 0
while j < len(newlist)-3:
    print(newlist[j])
    j += 1

#Looping through a list using list comprehension
# This will create a new list with the squares of the numbers in the original list
[print(x) for x in newlist]  

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
newlist1=[]
for x in newlist:
    if "a" in x:
        newlist1.append(x)
print(newlist1)

#Sorting a list: by default, the sort() method sorts the list in ascending order
newlist1.sort()
print(newlist1)
#Sorting a list in descending order
newlist1.sort(reverse=True)
print(newlist1)

#Using Functions to sort a list
def sort_by_length(newlist1):
    return len(newlist1)
newlist1.sort(key=sort_by_length)
print(newlist1)

newlist.reverse()
print(newlist)


#Copying a list
newlist2 = newlist.copy()
print(newlist2)     

newlist3= list(newlist)
print(newlist3)

newlist4 = newlist[:]
print(newlist4)

#Joining two lists
newlist5= newlist + newlist1
print(newlist5)

print(newlist.extend(newlist1))
