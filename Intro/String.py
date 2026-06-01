#Random Number Generator
import random
from tokenize import String
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

print(c[2:6])#Returns the characters from position 2 to 5 (not including 6)
print(c[-5:-1]) #Returns the characters from position -5 to -2 (not including -1)

#Uppercase and Lowercase and remove whitespace
print(c.upper())#Converts a string into upper case
print(c.lower())#Converts a string into lower case
print(c.strip())#Removes any whitespace from the beginning or the end of a string


#Replace String
print(txt.replace("free", "expensive"))#Replaces a string with another string


#Split String
print(txt.split(","))#Splits the string into substrings if it finds instances of the separator ";"  

#String Concatenation
a = "Hello"
b = "World"   
d=a+b
c = a + " " + b
print(d)
print(c)


#Format String
age = 36  
txt = f"My name is John, and I am {age}"
oor="My name is john, and I am {}"
print(txt)
print(oor.format(age))

#Placeholders and Modifiers
quantity = 3
itemno = 567      
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price*2)#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are. The first argument goes into the first placeholder, the second argument goes into the second placeholder, and so on. You can also use index numbers {0}, {1}, {2}, to specify which argument should be placed in which placeholder.
print(myorder)

#Escape Characters  
txt = "We are the so-called \"Vikings\" from the north." #To insert characters that are illegal in a string, use an escape character. An escape character is a backslash \ followed by the character you want to insert.
print(txt)    
#The all type of escape characters and their meaning are:
#\'	Single Quote    
#\"	Double Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace


#String Methods
txt = "hello, welcome to my world."
print(txt.capitalize())#Converts the first character to upper case  
print(txt.title())#Converts the first character of each word to upper case
print(txt.upper())#Converts a string into upper case
#Other string methods include:
#lower()	Converts a string into lower case
#strip()	Removes any whitespace from the beginning or the end
#replace()	Replaces a string with another string
#split()	Splits the string into substrings if it finds instances of the separator
#format()	Formats specified values in a string
#translate()	Returns a translated string
#zfill()	Fills the string with a specified number of 0 values at the beginning


#

