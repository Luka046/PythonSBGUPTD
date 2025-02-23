import json


def read_json_file(file_path):
    # Открываем JSON-файл для чтения
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)  # Загружаем данные из файла

        # Перебираем все продукты
        for product in data['products']:
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']}")
            print(f"Вес: {product['weight']}")

            # Проверяем наличие продукта
            if product['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")

            print()  # Пустая строка для разделения


#  путь к JSON-файлу
file_path = "products.json"
read_json_file(file_path)