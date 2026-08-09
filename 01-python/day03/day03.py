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
#-----------------------------------------------------------------------------------------------------------------

#Identity Operators: is, is not
'''
a = None
print(a is None)
print(a is not None)
'''
#Output:
'''
True
False
'''
#we frequently see:  if result is None:
#This is different from ==, 
#== asks: Do these values compare equal?
#is asks: Are these the same object?
#-----------------------------------------------------------------------------------------------------------------
'''
print("=" * 50)
print("PYTHON OPERATORS")
print("=" * 50)

a = 20
b = 6

print("\n--- Arithmetic ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print("\n--- Comparison ---")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

similarity_score = 0.82
minimum_score = 0.70

print("\n--- RAG Decision ---")

if similarity_score >= minimum_score:
    print("Document is relevant")
else:
    print("Document is not relevant")
'''

#Output:
'''
==================================================
PYTHON OPERATORS
==================================================

--- Arithmetic ---
Addition: 26
Subtraction: 14
Multiplication: 120
Division: 3.3333333333333335
Floor Division: 3
Remainder: 2
Power: 64000000

--- Comparison ---
a == b: False
a != b: True
a > b: True
a < b: False
a >= b: True
a <= b: False

--- RAG Decision ---
Document is relevant 
'''
#-----------------------------------------------------------------------------------------------------------------
'''
name = input("Enter your name: ")
daily_hours = float(input("How many hours can you study daily? "))
days = int(input("How many days do you want to study? "))

total_hours = daily_hours * days

print("\n===== STUDY PLAN =====")
print(f"Student: {name}")
print(f"Daily hours: {daily_hours}")
print(f"Study days: {days}")
print(f"Total study hours: {total_hours}")

if total_hours >= 300:
    print("Excellent commitment!")
elif total_hours >= 200:
    print("Good commitment!")
else:
    print("Keep increasing your consistency!")
'''

#Output:
'''
Enter your name: Bhagya
How many hours can you study daily? 2.5
How many days do you want to study? 120

===== STUDY PLAN =====
Student: Bhagya
Daily hours: 2.5
Study days: 120
Total study hours: 300.0
Excellent commitment!
'''
'''
x = 10
x += 5
x *= 2

print(x) 
'''
#output:30