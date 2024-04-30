class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"{flavor} is available.")
        else:
            print(f"{flavor} is not available.")

icecream_stand = IceCreamStand("Ice Cream Paradise", "Ice cream")
icecream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry"]

icecream_stand.display_flavors()
icecream_stand.check_flavor("Vanilla")
