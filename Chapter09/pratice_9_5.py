class User:
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"user full name {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_one = User("TongXin","Lu")
user_two = User("Tomas","Willen")

user_one.describe_user()
user_two.describe_user()

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.reset_login_attempts()
print(user_one.login_attempts)