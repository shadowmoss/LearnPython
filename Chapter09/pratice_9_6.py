from pratice_9_1 import Restaurant
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    
    def describe_flavors(self):
        for item in self.flavors:
            print(item)

flavors = ['sweat','hot','spicy']
iceCreamStand = IceCreamStand("IceCreamStand","west",flavors)
iceCreamStand.describe_flavors()