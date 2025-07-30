class Employee:
    def __init__(self,first,last,paycheck):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.email_id = first + '.' + last + '_@company.com'
        self.paycheck = 'Rs' + paycheck

    def fullname(self):     #METHOD 1
        return '{} {}'.format(self.first,self.last)

'''now we dont need to provide email it will be automatically printed'''
Employee_1 = Employee("arya","mourya","50000")
Employee_2 = Employee("Laxmi","mourya","600000")   
 
print(Employee_1.paycheck)
print(Employee_2.paycheck)

print(f"Hi my name is {Employee_1.first} {Employee_1.last} , I work in XYZ company .")
print(f"my email is {Employee_1.first + '.' + Employee_1.last + '_@company.com'}")  
print()

#rather than printing all this 2 above input code for writing full name . It better we create a method for full-name
#that def fullname.(self)