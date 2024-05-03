import random
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = []

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        res = random.randint(0, 1) # случайное значение от 0-1
        if res == 1:
            res1 = "открыт"
        else:
            res1 = "закрыт"
        print(f"Ресторан {self.restaurant_name} {res1}")


class IceCreamStand(Restaurant):
    def display_flavors(self):
        print("Доступные вкусы:")
        for flavor in self.flavors:
            print(flavor)
newRestaurant = Restaurant("Душа Востока", "грузинская")


# Вызываем оба метода
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Создаем экземпляр IceCreamStand
icecream_stand = IceCreamStand("Sweet Treats", "Ice Cream")
icecream_stand.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Мятное"]

icecream_stand.display_flavors()