
class Employee:
    raise_amount = 1.04  # Class variable
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first.capitalize(),self.last.capitalize())
    
    def raise_applied(self):
        self.pay ="Rs" + str((int(self.pay * self.raise_amount)))
        # self.pay ="Rs" + str((int(self.pay * Employee.raise_amount)))      

Employee_1 = Employee("arya","mourya",56000)
Employee_2 = Employee("Dona","rona",8900)

print(Employee.raise_amount)
print(Employee_1.pay)
Employee_1.raise_applied()            
print(Employee_1.pay)                  
#for the need to raise the pay of employee_1 and also
 #to apply the raise amount in employee_2 pay we need to write
# Employee_2.raise_applied() bt this may not be make our work easy so to make it easy we can use class variable
# and we can use it to apply the raise amount to all the employees at once.
'''if we use   self.pay ="Rs" + str((int(self.pay * 1.04))) it shows error because we are using instance variable'''
'''we need to use self.pay = "Rs" + str((int(self.pay * self.raise_amount))) or self.pay = "Rs" + str((int(self.pay * Employee.raise_amount)))'''



'''for that we need to use class variable and we can use it to apply the raise amount to all the employees at once.
   so we can use class variable to apply the raise amount to all the employees at once. by going to top of the class'''
'''the couple of thing wrong #Employee_1.raise_applied() method were:-
    * we need to apply this raise amount method to this employee class '''
''' Class-Variable = A variable that is shared by all instances/objects of a class.
   It is defined within the class but outside any instance methods.'''
# Class variables are accessed using the class name or through an instance of the class.
#class_var = "This is a class variable"
#like instance variable is unique to each instance, class variable should be same for each instance.