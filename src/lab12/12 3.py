def create_ru_en_dict(input_file, output_file):
    translations = {}  # Словарь для хранения перевода

    # Чтение англо-русского словаря
    with open(input_file, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Убираем лишние пробелы и символы новой строки
            if not line:  # Пропускаем пустые строки
                continue

            # Проверяем, что строка содержит разделитель " - "
            if " - " not in line:
                print(f"Ошибка: строка '{line}' не соответствует формату")
                continue

            # Разделяем строку на английское слово и русские переводы
            en_word, ru_words = line.split(" - ")

            # Разделяем русские переводы на отдельные слова
            for ru_word in ru_words.split(", "):
                if ru_word not in translations:
                    translations[ru_word] = set()  # Используем множество для хранения уникальных переводов
                translations[ru_word].add(en_word)  # Добавляем английское слово в множество

    # Запись русско-английского словаря в файл
    with open(output_file, mode='w', encoding='utf-8') as file:
        for ru_word in sorted(translations.keys()):  # Сортируем русские слова по алфавиту
            en_words = ", ".join(sorted(translations[ru_word]))  # Сортируем английские слова
            file.write(f"{ru_word} – {en_words}\n")  # Записываем строку в файл


# пути к файлам
input_file = "en-ru.txt"  # Исходный файл
output_file = "ru-en.txt"  # Выходной файл

# Создаем русско-английский словарь
create_ru_en_dict(input_file, output_file)
print("Русско-английский словарь создан!")