#Python Conditional Statements
#if, else,elif, Nested conditions,Multiple conditions,Indentation,Truthy / Falsy values,Basic conditional expressions,How conditions are used in RAG pipelines   

#if condition:
'''
a=15
if a>12:
    print(f"{a} is greater than 12")
'''
#output: 15 is greater than 12

#else condition:
'''
a=13
if a <= 12:
    print(f"{a} is less than or equal to 12")
else:
    print(f"{a} is greater than 12")
'''
 #OUTPUT: 13 is greater than 12

#elif condition:
'''
a=10
if a<10:
    print(f"{a} is less than 10")
elif a>10:
    print(f"{a} is greater than 10")
else:
    print(f"{a} is equal to 10")
'''
#output: 10 is equal to 10

'''
name=input("enter the name: ")
age=int(input("enter the age: "))
if name == "Bhagya":
     print(f"{age} is the age of {name}")
else:
     print(f"name is not Bhagya")
'''
'''
Name=[1,2,3,4,5]
if 6 in Name:
        print("1 is present in the list")
elif 2 in Name:
      print("2 is present in the list") 
else:
          print("6 and 2 are not present in the list")
'''