#function in python 

def sumfunc() :
    print("Arya Mourya")

sumfunc()
sumfunc()
sumfunc()


#practice question 
#1
def welcome_message():
    print("Welcome to Python Programming!")

welcome_message()
welcome_message()
welcome_message()

#2
def inspire():
    print("que serra que serra ~arya mourya")

inspire()

#3
def good_morning():
    print("Good Morning,Saumya!")

good_morning()
good_morning()

#4 (Simple function calling with no arguments)
def learn():
    print("function")
    print("dictionary")
    print("tuples")
learn()

##########Function Parameter & Arguments#######
def greet(name):
    print("Hello",name)
greet("Arya Mourya")
##2
def average(a,b):
    average_Value=(a+b)/2
    print(average_Value)
average(5,10)
average(3,7)
average(5,9)
##3
def add(a,b):
    Sum =(a+b)
    print("Sum =",Sum)
add(5,7)

"""PRACTICE QUESTIONS"""
#1
def show_age(name, age):
    print(f"{name} is {age}years old.")
show_age("Arya Mourya",16)
#2
def add_numbers(a , b):
    print(f"sum = {a+b}")
    print(f"difference = {a-b}")
add_numbers(9,5)

"""Default argument """
def greet(name="Saumya"):
    ptint("Hello",name)
greet()
greet("Riya")