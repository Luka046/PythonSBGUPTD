import os

def check_file_types(folder, extensions):
    for filename in os.listdir(folder):
        if filename.endswith(extensions):
            print(f"Найден файл: {filename}")

folder = "images"  # Папка с файлами
extensions = (".jpg", ".png")  # Допустимые расширения
check_file_types(folder, extensions)