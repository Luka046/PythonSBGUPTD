class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # Название ресторана
        self.cuisine_type = cuisine_type  # Тип кухни

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")