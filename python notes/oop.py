class student:
    name="Saumya Singh"
s1= student()
print(s1.name)

#1
class vehicle:#class creation
    color="red","blue"
    model="petrol-based","desiel-based"
#object creation
n2=vehicle()
print(n2.model)

"""practice question"""
class car:
    brand="scorpio"
p1=car()
print(p1.brand)
#2
class laptop:
    brand="default"
    RAM=28
    price="3lakh"

laptop1=laptop()
laptop1.brand="Lenovo"

laptop2=laptop()
laptop2.brand="hp"

print("Lptop Brand:",laptop1.brand)
print("Laptop brand:",laptop2.brand)

#3
class car:
    brand="scorpio"
    print("brand:",car.brand)

class student:
    college="XYZ college"
    def __init__(self,name):
        self.name=name

s1=student("Saumya")
print("Name:",s1.name)  
s2=student("Rohit")
print("Name:",s2.name)

"""PRACTICE QUESTION"""
#1
class FoodItem:
    category = "Snackes"

    def __init__(self, name):
        self.name = name

item1 =FoodItem("Samosa")
print("Category:",item1.name)

item2=FoodItem("Laddoo")
print("Category:",item2.name)

class Student:
    schoolName= "Notre Dame Academy"

    def __init__(self,name,course):
        self.name=name
        self.course=course

student1=Student("Arya","Btech")
print("Student1",student1.name)
print("Student1 Course-",student1.course)

student2=Student("Ankit","Msc")
print("Student2",student2.name,student2.course)