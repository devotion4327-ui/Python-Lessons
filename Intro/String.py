#Random Number Generator
import random
print(random.randint(1, 10))

#Multiline String
a = """This is a multiline string.
It can span multiple lines."""
print(a)                     


#Strings are Array
b = "Hello, World!"     
print(b[0])
print(b[2:5])

#Looping through a String
for x in "banana":
  print(x)      


#String Length
c = "Hello, World!"
print(len(c))   


#Check String: To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"   
print("free" in txt)    
print("expensive" in txt)
print("expensive" not in txt) #To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
if "expensive" not in txt: 
  print("No, expensive not present.")

#Slicing Strings

