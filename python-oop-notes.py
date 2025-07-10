class Person:
    name = "Arya"
    occupation = "Student"
    gender = "female"
    def info(self):
        print(f"{self.name} is a {self.occupation} .")

a = Person()
a.name = "Anu"
a.occupation = "Lawyer"
a.gender = "female"

print(a.name,a.gender,a.occupation)