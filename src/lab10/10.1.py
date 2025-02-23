from PIL import Image

def crop_image(image_path, output_path, left, top, right, bottom):
    try:
        image = Image.open(image_path)
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(output_path)
        print(f"Изображение обрезано и сохранено в {output_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

image_path = "example.jpg"  # Укажите путь к изображению
output_path = "cropped_image.jpg"
crop_image(image_path, output_path, 100, 100, 400, 400)  # координаты обрезки