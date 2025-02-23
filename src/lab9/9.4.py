from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_folder, output_folder, watermark_text):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    font = ImageFont.load_default()  # Используем стандартный шрифт
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), watermark_text, font=font, fill="white")
            output_path = os.path.join(output_folder, f"watermarked_{filename}")
            image.save(output_path)
            print(f"Добавлен водяной знак: {filename}")

input_folder = "images"  # Папка с исходными изображениями
output_folder = "watermarked_images"  # Папка для сохранения изображений с водяным знаком
watermark_text = "Sample Watermark"
add_watermark(input_folder, output_folder, watermark_text)