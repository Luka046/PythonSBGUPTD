from PIL import Image

def show_holiday_card(holiday, cards_dict):
    if holiday in cards_dict:
        image_path = cards_dict[holiday]
        try:
            image = Image.open(image_path)
            image.show()
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        print("Праздник не найден.")

cards_dict = {
    "Новый год": "new_year.jpg",
    "Рождество": "christmas.jpg",
    "8 Марта": "womens_day.jpg"
}

holiday = input("Введите праздник: ")
show_holiday_card(holiday, cards_dict)