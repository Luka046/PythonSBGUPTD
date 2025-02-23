from PIL import Image

def show_image_info(image_path):
    try:
        image = Image.open(image_path)
        print("Формат изображения:", image.format)
        print("Размер изображения:", image.size)
        print("Цветовая модель:", image.mode)
        image.show()  # Открытие изображения
    except Exception as e:
        print(f"Ошибка: {e}")

image_path = "zona.jpg"  # путь к изображению
show_image_info(image_path)