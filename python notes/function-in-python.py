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
def show_age(name="laxmi", age=18):
    print(f"{name} is {age}years old.")
show_age("Arya Mourya",16)
show_age()
#2
def add_numbers(a , b):
    print(f"sum = {a+b}")
    print(f"difference = {a-b}")
add_numbers(9,5)

"""Default argument """
#a
def greet(name="Saumya"):
    print("Hello",name)
greet()
greet("Riya")
"""Return statements"""
def add(a,b):
    return a+b 
result = add(10,20)
print("Result =",result)
#practice question:
##1.
def square(num=10):
    return num**2
print(square(3))
##2.

def multiply(a=10, b=10):
    return a*b

result= multiply(5,10)
print(result)
#
def multiply(a=10,b=10):
    return a*b
print(multiply(5,5))

"""Practice question """
#1
def square(num):
    return num**2
print(square(2))
#2
def function(userInput):
    #define vowels
    vowels = "aeiouAEIOU"

    countVowels=0
    countConsonants=0

    for eachChar in userInput:
       if(eachChar.isalpha()): #will check that is all character is alphabate
           if(eachChar in vowels): #will check that is all character is volume
               countVowels=countVowels+1 #
           else:
               countConsonants+=1
    
    return countVowels,countConsonants

#Function Call
vowels,consonants=function("Arya Mourya")

print(vowels,consonants)
"""Practice questions """
def message(text="Keep Learning"):
    print(text)
    message()
    message("done learning")

####Variable scope####
x=10 #global variable\
def show():
    x=5 #local variable\
    print("Inside function:",x)

show()
print("Outside function:",x)