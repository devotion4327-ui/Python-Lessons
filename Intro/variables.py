x=5
y="Soorya Kumar"#string variable
print(y,"is",x,"years old.")

#casting: to specify the data type of a variable
z=str(5)#casting the integer 5 to a string
a=int(5)#casting the integer 5 to an integer (not necessary in this case)
b=float(5)#casting the integer 5 to a float

#string can be declared using single or double quotes
c='Hello, World!'#string variable using single quotes
d="Hello, World!"#string variable using double quotes

#Assigning multiple values to multiple variables
e,f,g="Soorya","Kumar",25
print(e,f,g)

#List or tuple unpacking: assigning values from a list or tuple to variables
h=["Soorya","Kumar",25]#a list containing three elements
i,j,k=h #unpacking the list into variables
print(i,j,k)

#Other methods of outputting variables
l="Soorya Kumar"
m=' 25'
print(l+m)

#Global variables: variables that are defined outside of a function and can be accessed inside the function
n="I am a global variable"
def my_function():
    print(n) #accessing the global variable inside the function

my_function()#calling the function to see the output of the global variable

#Global keyword: used to declare a variable as global inside a function, allowing you to modify the global variable
def my_function2():
    global n #declaring n as a global variable
    n="I have been modified inside the function" #modifying the global variable inside the function
my_function2()#calling the function to modify the global variable
print(n) #printing the modified global variable 

