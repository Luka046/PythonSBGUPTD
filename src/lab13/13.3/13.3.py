from restaurant import Restaurant

class RatedRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        super().__init__(restaurant_name, cuisine_type)
        self.rating = initial_rating

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен: {self.rating}")

rated_restaurant = RatedRestaurant("Вкусно и точка", "итальянская", 4.5)
rated_restaurant.describe_restaurant()
rated_restaurant.update_rating(4.8)