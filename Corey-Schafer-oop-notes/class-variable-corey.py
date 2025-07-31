class Employee:
    def __init__(self,first,last,paycheck):
        self.first = first
        self.last = last
        self.email_id = first + '.' + last + '_@company.com'
        self.paycheck = 'Rs' + paycheck

        def fullname(self):   
          return '{} {}'.format(self.first.capitalize(),self.last.capitalize())
        
Employee_1 = Employee("arya","mourya","50000")
Employee_2 = Employee("Laxmi","mourya","600000")  
