name = "Arya"
age = 19

print(name.upper())
print(type(age))

#introduction
class Dog :
    def __init__(self,name,breed,Owner):
         self.name = name
         self.breed = breed 
         self.Owner = Owner

    def bark(self):
        print("Woof Woof")

class Owner :
    def __init__(self,name,address,contact_number,emailID):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.emailID = emailID
    
    def introduction(self,Dog):
        print(f"Hi!,I'm {self.name},I lives {self.address} .I would like to introduce you to my pet .")
        print(f"This is {Dog.name} ,my pet dog and he is a {Dog.breed}")


Owner1 = Owner("Rikki","xyz road","0000123499","rikki01@gmail.com")
dog1 = Dog("Bruce","Pitbull",Owner1)
dog1.bark()
Owner1.introduction(dog1)
print(dog1.name)
print(dog1.breed)
print(dog1.Owner.name)
print(dog1.Owner.contact_number,dog1.Owner.emailID)

Owner2 = Owner("Simmi","abcd road","999993447","simmi23@gmail.com")
dog2 = Dog("Freya","ScoOwner1ttish Terrior",Owner2)
dog2.bark()
Owner2.introduction(dog2)
print(dog2.name)
print(dog2.breed)
print(dog2.Owner.contact_number,dog2.Owner.emailID)

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def greet(self):    #here we give behaviour or a method to each given person to greet.
        print(f"Hi, My name is {self.name} and I am {self.age}years old.")

Person1 = Person("Ginger",40)
Person1.greet()

Person2 = Person("Garly",32)
Person2.greet()