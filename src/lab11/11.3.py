import csv


def read_csv_file(file_path):
    total_cost = 0  # Итоговая сумма расходов
    print("Нужно купить:")

    # Открываем CSV-файл для чтения
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Читаем файл как словарь
        for row in reader:
            product = row['Продукт']  # Название продукта
            quantity = int(row['Количество'])  # Количество
            price = int(row['Цена'])  # Цена за единицу
            cost = quantity * price  # Стоимость продукта
            total_cost += cost  # Добавляем к итоговой сумме

            # Выводим информацию о продукте
            print(f"{product} - {quantity} шт. за {price} руб.")

    # Выводим итоговую сумму
    print(f"Итоговая сумма: {total_cost} руб.")


# путь к CSV-файлу
file_path = "products.csv"
read_csv_file(file_path)