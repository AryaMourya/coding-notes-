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
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

Owner1 = Owner("Rikki","xyz road","0000123499")
dog1 = Dog("Bruce","Pitbull",Owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.Owner.name)


Owner2 = Owner("Simmi","abcd road","999993447")
dog2 = Dog("Freya","ScoOwner1ttish Terrior")
dog2.bark()
print(dog2.name)
print(dog2.breed)