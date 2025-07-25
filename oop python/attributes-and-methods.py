''' ( ATTRIBUTES and METHODS )'''
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self,user):
        print(
        f"Sending message to {user.username}: Hi {user.username},it's {self.username}"
        )
'''self.username == Username of the caller object (User_1 -> Sammy)
         {refers to instance's own data} '''
'''user.username == Username of the passed objects (User_2 -> Anna)
             {Refers to another object}'''

User_1 = User("Sammy","sammy01@gmail.com","23qw")
User_2 = User("Anna","anna28@gmail.com","345d")

User_1.say_hi_to_user(User_2)  #What it say ?
                 # Hey User_1 ,please use your say_hi_to_user() method and pass
                 # User_2 as the argument .
'''User_1.say_hi_to_user(User_2)  === Sammy greets Anna 
                {Method call with self + user} '''


##MODIFICATION objects data 
ser_1 = User("Sammy","sammy01@gmail.com","23qw")
print(User_1.email)
User_1.email = "sammy234@gmail.com"
print(User_1.email)

#Accessing and Modifying Data :
# 1. The traditional way: make the data private and use getters and setters: