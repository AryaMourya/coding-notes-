# Object Orinated Programming

class employee:   #class
    pass
emp1 = employee()
emp2 = employee()   
''' this above given employe 1 and 2 are class instance'''

print(emp1)
print(emp2)

emp1.first = "Aru"
emp1.last = "anna"
emp1.email = "aru01@gmail.com"
emp1.pay = "$5000"

emp2.first = "elsa"
emp2.last = "anna"
emp2.email = "elsaanna34@gmail.com"
emp2.pay = "$4500"

print(emp1.email)
print(emp2.email)
'''to make these setup automatic we create the employee we are going to use special method of
 init in this'''

def __init__(self,first,last,):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '-' + last + "compay.com"
