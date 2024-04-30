class restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the restaurant {self.name} serves {self.cuisine_type} cuisine.")

class icecreamstand(restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Ice cream flavors available:")
        for flavor in self.flavors:
           print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"{flavor} added to flavors list.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"{flavor} removed from flavors list.")
        else:
            print(f"{flavor} is not in flavors list.")

ice_cream_stand = icecreamstand("Ice Cream Stand", "Ice Cream")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry"]

# вызываем методы для объекта ice_cream_stand
ice_cream_stand.display_flavors()
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.remove_flavor("Mint")
