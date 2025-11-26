from pratice_9_5 import User
class Admin(User):

    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges=privileges
    
    def show_privileges(self):
        for item in self.privileges:
            print(item)

privileges = ["add","delete","select"]
admin = Admin("Tomas","willen",privileges)
admin.show_privileges()