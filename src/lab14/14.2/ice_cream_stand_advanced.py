from ice_cream_stand import IceCreamStand

class AdvancedIceCreamStand(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type, flavors)
        self.location = location
        self.working_hours = working_hours

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт '{flavor}' добавлен.")
        else:
            print(f"Сорт '{flavor}' уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удален.")
        else:
            print(f"Сорт '{flavor}' не найден.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт '{flavor}' есть в наличии.")
        else:
            print(f"Сорт '{flavor}' отсутствует.")

ice_cream_stand = AdvancedIceCreamStand(
    "Мороженка", "десерты", ["ванильное", "шоколадное"], "ул. Ленина, 10", "10:00 - 22:00"
)
ice_cream_stand.show_flavors()
ice_cream_stand.add_flavor("клубничное")
ice_cream_stand.check_flavor("клубничное")
ice_cream_stand.remove_flavor("ванильное")
ice_cream_stand.show_flavors()