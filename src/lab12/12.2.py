import json

def add_product_to_json(file_path):
    name = input("Введите название продукта: ")
    price = float(input("Введите цену: "))
    available = input("Есть в наличии? (да/нет): ").lower() == "да"
    weight = float(input("Введите вес: "))

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    data['products'].append(new_product)

    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Продукт добавлен!")

file_path = "products.json"  # путь к JSON-файлу
add_product_to_json(file_path)