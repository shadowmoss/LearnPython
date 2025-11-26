class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_type(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

my_restaurant = Restaurant("my_restaurant","west_style")
print(f"name = {my_restaurant.restaurant_name},type = {my_restaurant.cuisine_type}")
my_restaurant.open_restaurant()