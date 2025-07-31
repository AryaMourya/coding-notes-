class Employee:
    def __init__(self,first,last,paycheck):
        self.first = first
        self.last = last
        self.email_id = first + '.' + last + '_@company.com'
        self.paycheck = paycheck
        
        def apply_raise(self):
           self.paycheck =  self.paycheck * 1.04

Employee_1 = Employee("arya","mourya",50000)
Employee_1.apply_raise()
 

''' Class-Variable = A variable that is shared by all instances of a class.
   It is defined within the class but outside any instance methods.'''
# Class variables are accessed using the class name or through an instance of the class.
#class_var = "This is a class variable"
#like instance variable is unique to each instance, class variable should be same for each instance.
