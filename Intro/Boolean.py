# Boolean Values
is_raining = True
is_sunny = False

print(is_raining)  # True
print(is_sunny)   # False

#bool() function
print(bool(0))    # False   
print(bool(1))    # True
print(bool(""))   # False
print(bool("Hello"))  # True

#Functions that return boolean values
def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False      

#isinstance() function
x = 10      
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False

## Print the result of 10 > 9
print(10 > 9)  # True
## Print the result of 10 == 9
print(10 == 9)  # False 



