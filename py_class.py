# JawnPythias
# date:22/02/2024

# 创建类的一个练习
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now operating!")

    def set_number_served(self, value):
        self.number_served = value

    def increment_number_served(self):
        self.number_served += 1

restaurant = Restaurant("111", "China", 45)
restaurant.set_number_served(23)
restaurant.increment_number_served()
print(restaurant.number_served)

# 继承
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavours):
        super().__init__(restaurant_name, "Sweet", 100)
        self.flavours = flavours

    def show_flavours(self):
        print(self.flavours)

icestand = IceCreamStand("222", ["bananas", "apple", "candy"])
icestand.show_flavours()
icestand.describe_restaurant()