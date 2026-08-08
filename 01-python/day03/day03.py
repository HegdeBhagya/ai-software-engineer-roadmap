'''
Today's goals:
Arithmetic operators
Comparison operators
Logical operators
Assignment operators
in / not in
is / is not
How Python evaluates expressions
A small practical project
Interview questions
'''
#------------------------------------------------------------------------------------------------------------------
#Arithmetic operators
'''
a=10
b=13
c=2
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division : /Always gives a decimal (float)
print(a // c)  # Floor division : 10 // 3 Result:3
print(a % b)   # Modulus : Gives the remainder
print(a ** c)  # Power
'''
#output:
'''
23
-3
130
0.7692307692307693
5
10
100
'''
#-----------------------------------------------------------------------------------------------------------------

#Comparison Operator
'''
age = 25
print(age == 25)
print(age != 30)
print(age > 18)
print(age < 30)
print(age >= 26)
print(age <= 25)
'''
#common interview question.
'''
"=" means assignment
"==" means comparison.
Example:
age = 25, means:Put 25 into age.
age == 25, means: Is age equal to 25?
'''
#output:
'''
True
True
True
True
False
True
'''
#-----------------------------------------------------------------------------------------------------------------

#Logical Operators
#and:For and, both conditions must be True.
#or:For or, at least one condition must be True.
#not:Reverse the result, returns False if the result is True.
'''
age1 = 25
age2 = 80
print(age1 >= 18 and age2 >= 60)
print(age1>=age2 and 2>=age1)
print(not True)
'''
#output
'''
True
False
False
'''
#-----------------------------------------------------------------------------------------------------------------

#Assignment Operators
'''
x = 10
print(x)
x += 5 # which means:x=x+5
print(x)
x = 10
x -= 2
print(x)
x = 10
x *= 3
print(x)
x = 10
x /= 2
print(x)
'''
#output:
'''
10
15
8
30
5.0
'''
#-----------------------------------------------------------------------------------------------------------------

#Membership Operators
'''
languages = ["Python", "Java", "C#"]

print("Python" in languages)
print("javascript" not in languages)
'''
#output:
'''
True
True
'''
