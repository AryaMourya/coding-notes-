character_name="Arya"
character_age="19"
print("There one was a person named "+ character_name+",")
print(f"He was {character_age} years old. ")
print("he was "+character_age+ " years old.")
print(f"My name is {character_name}.\nI am {character_age} years old.")
print(character_name)
fruit="Apple"
print(fruit.lower() + " is my favourite fruit.")
print(fruit.upper() + " is my favourite fruit.")
print(fruit.upper().isupper())
print(fruit[0:])
print(fruit.index("A"))
print(f"You like {fruit.replace("Apple","mango")} as a summer fruit.")
y=-5
z =abs(y) * 3 #abs
x =pow(3,3) / 3  #POW()
print(max(x,z))   #max()  OR #min()

from math import*
print(floor(3.147))
print(ceil(3.147))
print(sqrt(144))
print(f"{pi:.3f}")

##LIST##
friends = ["ami","ana","emma"]
friends[1]="meena"
print(friends[1])

##LIST FUCTIONS
wildife=animal=["lion","tiger","zebra"]
birds=["crow","spparow","parrot"]
animal.extend(birds)   #List.extend()
print(wildife)
animal.append("cow")   #List.append()
print(animal)
animal.insert(2,"fox")   #List.intrest(position,new added element)
print(animal)
list_1=["x","a","x","y"]
list_1.remove("a")
print(list_1)
friends.clear()  #List.clear()
print(friends)   #List.pop()
animal.pop()
#Print(List.index(" "))
print(animal.index("lion"))
#List.sort()
animal.sort()
print(animal)
# list2=list1.copy()
bird2=birds.copy()
print(bird2)
##TUPLES
#how to create?
coordinate=(4 ,5)
print(coordinate[0])

#When we use TUPLES and LISTS together.
coordinates=[(4,5),(8,6),(7,3)]
print(coordinates[2])


##FUCTIONS:-
#1)
def say_hi():
    print("Hello User!")
print("Hi! Arya.")
say_hi()
print("How are you ?")
#2)
def say_hi(name,age):
    print(f"Hello, {name} .Your age is {age}years old.")

say_hi("Arya","19")
say_hi("Laxmi","17")

## return statement:
def cube(num):
    return num*num*num

print(cube(4))
print(cube(3))

#If,elif and else
#1)
is_female=True
is_tall=False

if is_female and is_tall:
    print("You are a female and tall.")
else:
    if is_tall:
     print("You are tall , you are not a female.")
    elif is_female:
        print("You are female but not tall.")
    else:
        print("You neither female nor your tall .")

## If statement and comparisions:
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num1>=num3:
        return num2
    else:
        return num3
    
print(max_num(4,4,4))

##DICTIONARIES:-
Monthly_Conversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "July":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
print(Monthly_Conversions["Nov"])
#OR
print(Monthly_Conversions.get("Apr"))
print(Monthly_Conversions.get("Luv,Not a valid key."))

##While loop:
i=1
while i <=10:
    print(i)
    i += 1

print("Run this loop")

# Guessing Game:-
secret_word = "giraffe"
guess =""
guess_count=0
guess_limit=3
out_of_guesses=False
hint_taken=False
while guess !=secret_word and not out_of_guesses:
    if guess_limit > guess_count:
      guess = input("Enter guess: ")
      guess_count+=1
      if not hint_taken and guess !=secret_word:
         hint=input("DO you want hints? (Yes/No):")
         if hint=="Yes":
           print ("wild animal," \
                   "eat grass," \
                   "has long neck")
         elif hint=="No":
              print("OK!")
    else:
        out_of_guesses=True
       
if out_of_guesses==True:
 print("You lose!")
else:
  print("You Win!")
##For LOOP
#1)
for letter in "apple" :
   print(letter)
#2)
for x in range(1,11):
   print(x)
#3)
for x in reversed(range(1,11)):
   print(x)
#4)
for x in range(1,11,-1):
   print(x)
#5)
for x in  range(1,11,2):
   print(x)
#6)
friends=["ken","mina","jennie"]
for name in friends:
   print(name)
#7)good example
friends=["ken","mina","jennie"]
for index in range(len(friends)):
   print(index)
   print(friends[index])
#8)
for index in range(5):
   if index== 0:
      print("First Iteration")
   else:
      print("Not First Iteration ")
## Exponent functions:-
def raise_to_power(base_num,pow_num):
   result = 1
   for index in range(pow_num):
      result= result* base_num
   return result

print(raise_to_power(3 , 2))

###2D lists and nested loop :-
number_grid =[
   [1,2,3],
   [4,5,6],
   [7,8,9],
   [0]
]
print(number_grid[0][0])
print(number_grid[1])
#Nested loop:-
#1)
for row in number_grid:
   print(row)
#2)
for row in number_grid:
   for col in row:
      print(col)

###Try/Except
number = int(input("Enter the number:"))
print(number)
'''if we enter wrong variable and after running the code it shows error .
To overcome this problem we use Try/Except '''

try:
    number = int(input("Enter the number:"))
    print(number)
except:
   print("Invalid Input")
try:
   value=10/0
   number = int(input("Enter the number:"))
   print(number)
except ZeroDivisionError:
   print("Divided by zero ")
except ValueError:
   print("Invalid Input")
except ZeroDivisionError as err:
   print(err)

###READING FILES###
