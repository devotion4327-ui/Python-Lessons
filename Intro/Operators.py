#Arithmetic Operators
a = 10
b = 5
print(a + b)  # 15 # Addition
print(a - b)  # 5 # Subtraction
print(a * b)  # 50 # Multiplication
print(a / b)  # 2.0 # Division
print(a % b)  # 0 # Modulus
print(a ** b) # 100000 # Exponentiation
print(a // b) # 2 # Floor division

#Comparison Operators
print(a > b)   # True # Greater than
print(a < b)   # False # Less than
print(a == b)  # False # Equal to
print(a != b)  # True # Not equal to
print(a >= b)  # True # Greater than or equal to
print(a <= b)  # False # Less than or equal to

#Logical Operators
x = True
y = False
print(x and y)  # False # AND
print(x or y)   # True # OR
print(not x)    # False # NOT
print(not y)    # True # NOT

#Assignment Operators
c = 10
c += 5  # c = c + 5# c is now 15
c -= 3  # c = c - 3# c is now 12    
c *= 2  # c = c * 2# c is now 24
c /= 4  # c = c / 4# c is now 6.
c %= 5  # c = c % 5# c is now 1.0
c **= 3 # c = c ** 3# c is now 1.0
c //= 2 # c = c // 2# c is now 0.

#Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

#Comparison Operators
print(10 > 9)  # True # Greater than
print(10 < 9)  # False # Less than  
print(10 == 9) # False # Equal to
print(10 != 9) # True # Not equal to
print(10 < 9)  # False # Less than or equal to
print(10 >= 9) # True # Greater than or equal to
print(10 <= 9) # False # Less than or equal to
print(10 != 9) # True # Not equal to

#Logical Operators
print(True and False)  # False # AND
print(True or False)   # True # OR
print(not True)        # False # NOT
print(not False)       # True # NOT

#Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # False # x and y are different objects in memory
print(x == y)  # True # x and y have the same content
print(x is not y) # True # x and y are different objects in memory

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True # "banana" is in the list
print("grape" in fruits)   # False # "grape" is not in the list
print("grape" not in fruits) # True # "grape" is not in

#Bitwise Operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print(a & b)  # 1  # AND # In binary: 0001 # Both bits are 1 # Only the last bit is 1
print(a | b)  # 7  # OR # In binary: 0111 # At least one bit is 1
print(a ^ b)  # 6  # XOR # In binary: 0110 # Bits are different
print(~a)       # -6  # NOT # In binary: ...11111010 # Flips all bits
print(a << 1) # 10  # Left shift # In binary: 1010 # Shifts bits left
print(a >> 1) # 2   # Right shift # In binary: 0010 # Shifts bits right

#Operator Precedence
result = 10 + 5 * 2  # Multiplication is performed before addition
print(result)  # 20
result = (10 + 5) * 2  # Parentheses change the order of operations
print(result)  # 30
#Precedence Order
#1. Parentheses ()
#2. Exponentiation (**)
#3. Unary plus and minus (+x, -x)
#4. Multiplication, Division, Modulus, Floor division (*, /, %, //)
#5. Addition and Subtraction (+, -)
#6. Bitwise Shift Operators (<<, >>)
#7. Bitwise AND (&)
#8. Bitwise XOR (^)
#9. Bitwise OR (|)
#10. Comparison Operators (==, !=, >, <, >=, <=)
#11. Identity Operators (is, is not)
#12. Membership Operators (in, not in)
#13. Logical NOT (not)
#14. Logical AND (and)
#15. Logical OR (or)


#Operator Associativity
result = 10 - 5 - 2  # Subtraction is left-associative
print(result)  # 3 # (10 - 5) - 2
result = 2 ** 3 ** 2  # Exponentiation is right-associ
print(result)  # 512 # 2 ** (3 ** 2)

#Augmented Assignment Operators
x = 10
x += 5  # x = x + 5 # x is now 15
x -= 3  # x = x - 3 # x is now 12
x *= 2  # x = x * 2 # x is now 24   
x /= 4  # x = x / 4 # x is now 6.
x %= 5  # x = x % 5 # x is now 1.0
x **= 3 # x = x ** 3 # x is now 1.
x //= 2 # x = x // 2 # x is now 0.

