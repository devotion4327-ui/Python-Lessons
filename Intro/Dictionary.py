# Python dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",      
    "model": "Mustang",
    "year": 1964
}   
print(thisdict)
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Access Elements:
x=thisdict["brand"]
y=thisdict.get("model")

print(x,y)

#Gets values:
z= thisdict.values()
print(z)

#Add Iteam:
thisdict["color"]="green"
print(thisdict)

#to remove:

thisdict.pop("model")
print(thisdict)

#Looping
for i in thisdict:
    print(i)
for j in thisdict:
    print(thisdict[j])

for m,n in thisdict.items():
    print(m,n)

#Copy a dictionary:
newdict=thisdict.copy()
print(newdict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print(myfamily["child2"]["name"])

