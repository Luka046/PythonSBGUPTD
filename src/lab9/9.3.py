from PIL import Image, ImageFilter
import os

def apply_filter_to_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            # Применение фильтра 
            filtered_image = image.filter(ImageFilter.CONTOUR)
            output_path = os.path.join(output_folder, f"filtered_{filename}")
            filtered_image.save(output_path)
            print(f"Обработано: {filename}")

input_folder = "images"  # Папка с исходными изображениями
output_folder = "filtered_images"  # Папка для сохранения обработанных изображений
apply_filter_to_images(input_folder, output_folder)