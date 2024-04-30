class Restaurant:
    def __init__(self, name, cuisine_type):  # метод __init__
        self.name = name # self ссылка на экземпляр объекта
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):  # атрибут flavors
        # super позволяет получить доступ к атрибутам, ссылка на тип класса
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Ice cream flavors available:")
        for flavors in self.flavors:
            print(flavors)

# создается объект ice_cream_stand класса icecreamstand c аргументами name b flavors
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Cherry", "Mint"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
