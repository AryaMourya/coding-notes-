''' ( ATTRIBUTES and METHODS )'''
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def __init_(self,user):
        print(
        f"Sending message to {user.username}: Hi {user.username},it's {self.username}"
        )

User_1 = User("Sammy","sammy01@gmail.com","23qw")
User_2 = User("Anna","anna28@gmail.com","345d")