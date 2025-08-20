raise_amount = 1.04



class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first.capitalize(),self.last.capitalize())
    
    def raise_applied(self):
        self.pay ="Rs" + str((int(self.pay * 1.04)))

Employee_1 = Employee("arya","mourya",56000)
Employee_2 = Employee("Dona rona",8900)

print(Employee_1.pay)
Employee.raise_applied()
print(Employee.pay)

''' Class-Variable = A variable that is shared by all instances of a class.
   It is defined within the class but outside any instance methods.'''
# Class variables are accessed using the class name or through an instance of the class.
#class_var = "This is a class variable"
#like instance variable is unique to each instance, class variable should be same for each instance.