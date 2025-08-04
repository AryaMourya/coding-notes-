class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first.capitalize(),self.last.capitalize())
    
    def raise_applied(self):
        self.pay = int(self.pay * 1.04)

Employee_1 = Employee("arya","mourya",56000)

print(Employee_1.pay)
Employee_1.raise_applied()
print(Employee_1.pay)