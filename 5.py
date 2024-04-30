class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the restaurant {self.name} serves {self.cuisine_type} cuisine.")

class IcecreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
        self.stick_icecream = []
        self.soft_serve_icecream = []

    # метод add добавляет новые сорта мороженого в списки
    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def add_stick_icecream(self, flavor):
        self.stick_icecream.append(flavor)

    def add_soft_serve_icecream(self, flavor):
        self.soft_serve_icecream.append(flavor)

    # метод describe выводит информацию о доступных вариантах мороженого каждого типа
    def describe_icecream_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)

    def describe_stick_icecream(self):
        print("Available stick ice cream flavors:")
        for flavor in self.stick_icecream:
            print(flavor)

    def describe_soft_serve_icecream(self):
        print("Available soft serve ice cream flavors:")
        for flavor in self.soft_serve_icecream:
            print(flavor)


ice_cream_shop = IcecreamStand("Sweet Treats", "Ice Cream")

# добавляем сорта мороженого
ice_cream_shop.add_flavor("Vanilla")
ice_cream_shop.add_flavor("Chocolate")
ice_cream_shop.add_stick_icecream("Strawberry")
ice_cream_shop.add_soft_serve_icecream("Mint")

# вызываем методы для вывода списка каждого типа мороженого
ice_cream_shop.describe_icecream_flavors()
ice_cream_shop.describe_stick_icecream()
ice_cream_shop.describe_soft_serve_icecream()
