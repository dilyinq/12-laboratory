class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant {self.name} provides {self.cuisine_type}.")
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors, location, opening_hours):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.opening_hours = opening_hours

    def display_flavors(self):
        print("Ice cream flavors available:")
        for flavor in self.flavors:
            print(flavor)

    def describe_location(self):
        print(f"The ice cream cafe is located at {self.location}.")

    def describe_opening_hours(self):
        print(f"The ice cream cafe is open from {self.opening_hours}.")

ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry","Cherry","Mint"], "Moskovsky Prospek, 21A", "10:00-21:00")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
ice_cream_stand.describe_location()
ice_cream_stand.describe_opening_hours()

