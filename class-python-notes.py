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
is_tall=True

if is_female:
    print("You are a female.")
else:
    print("Your are not female")
