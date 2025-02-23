from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, output_path, text):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  # Используем стандартный шрифт
        draw.text((50, 50), text, font=font, fill="red")
        image.save(output_path)
        print(f"Текст добавлен, изображение сохранено в {output_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

image_path = "example.jpg"  # Укажите путь к изображению
output_path = "text_image.png"
text = input("Введите текст: ")
add_text_to_image(image_path, output_path, text)