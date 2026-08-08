#Datatypes
'''
Name="Bhagya"
age=25

print(Name)
print(age)

name=input("Enter your name: ")
age=input("Enter your age: ")
age1=int(input("Age: "))

print(name)
print(age)
print(age1)

print(age + 1)   # throws error because age is a string , we need to convert it into integer before adding 1 to it
print(age1 + 1)
'''
# Output
'''
Bhagya
25
Enter your name: Ramu
Enter your age: 34
Age: 35
Ramu
34
35
Traceback (most recent call last):
  File "D:\AI-Roadmap-2026\AI-Learning\ai-software-engineer-roadmap\01-python\day02\day02.py", line 16, in <module>
    print(age + 1)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
'''



#Code for AI Engineer Learning Tracker
'''
print("=" * 50)
print("AI Engineer Learning Tracker")
print("=" * 50)

name = input("Enter your name: ")
role = input("Target role: ")
study_hours = float(input("Daily study hours: "))
study_hours1 = input("Daily study hours: ")
python_level = input("Python Level: ")

weekly_hours = study_hours * 7

print("\n===== SUMMARY =====")
print(f"Name          : {name}")
print(f"Target Role   : {role}")
print(f"Python Level  : {python_level}")
print(f"Daily Hours   : {study_hours}")
print(f"Weekly Hours  : {weekly_hours}")

print("\nKeep showing up every day! 🚀")
print(type(name))
print(type(study_hours))
print(type(study_hours1))
'''
#Output
'''
==================================================
AI Engineer Learning Tracker
==================================================
Enter your name: Bhagya
Target role: AI Engineer
Daily study hours: 3
Daily study hours: 3
Python Level: Intemediate

===== SUMMARY =====
Name          : Bhagya
Target Role   : AI Engineer
Python Level  : Intemediate
Daily Hours   : 3.0
Weekly Hours  : 21.0

Keep showing up every day! 🚀
<class 'str'>
<class 'float'>
<class 'str'>
'''
age = "20"
print(age * 3) #output: 202020

age1 = 21
print(age1 * 3) #output:63

year=input()  
print(type(year))
#output
'''
Nothing is printed to the screen. Instead, Python waits for you to enter something.
For example, when you run:
age = input()
the terminal will appear blank: |
Python is waiting for input.
If you type:
25
and press Enter, then: age contains: "25"
Notice the quotes conceptually — age is a string, not a
'''