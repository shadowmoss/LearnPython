class User:
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"user full name {self.first_name} {self.last_name}")

user_one = User("TongXin","Lu")
user_two = User("Tomas","Willen")

user_one.describe_user()
user_two.describe_user()