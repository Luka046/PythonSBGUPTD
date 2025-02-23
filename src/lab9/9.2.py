from PIL import Image, ImageOps

def process_image(image_path):
    try:
        image = Image.open(image_path)
        # Уменьшение в 3 раза
        resized_image = image.resize((image.width // 3, image.height // 3))
        resized_image.save("resized_image.jpg")

        # Горизонтальное зеркальное отражение
        mirrored_horizontal = ImageOps.mirror(image)
        mirrored_horizontal.save("mirrored_horizontal.jpg")

        # Вертикальное зеркальное отражение
        mirrored_vertical = ImageOps.flip(image)
        mirrored_vertical.save("mirrored_vertical.jpg")

        print("Изображения сохранены.")
    except Exception as e:
        print(f"Ошибка: {e}")

image_path = "zona.jpg"  # путь к изображению
process_image(image_path)