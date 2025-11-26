class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_type(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,served):
        self.number_served += served
    
my_restaurant = Restaurant("my_restaurant","west_style")
print(f"name = {my_restaurant.restaurant_name},type = {my_restaurant.cuisine_type}")
my_restaurant.open_restaurant()

my_restaurant.number_served = 100
print(my_restaurant.number_served)

my_restaurant.set_number_served(50)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(200)
print(my_restaurant.number_served)