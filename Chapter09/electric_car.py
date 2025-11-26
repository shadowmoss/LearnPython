from car import Car
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        # self.battery_size = 40
        self.battery = Battery()
    
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery.battery_size}-kWh battery")
    
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")
class Battery:
    """一次模拟电动汽车电池的简单尝试"""

    def __init__(self,battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('audi','a6',2025)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.battery.describe_battery()