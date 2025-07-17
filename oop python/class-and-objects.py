name = "Arya"
age = 19

print(name.upper())
print(type(age))

#introduction
class Dog :
    def __init__(self,name,breed):
         self.name = name
         self.breed = breed 

    def bark(self):
        print("Woof Woof")

dog1 = Dog("Bruce","Pitbull")
dog1.bark()

dog2 = Dog("Freya","Scottish Terrior")
dog2.bark()